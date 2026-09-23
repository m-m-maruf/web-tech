package main

import (
	"crypto/rand"
	"encoding/base64"
	"encoding/json"
	"net/http"
	"sync"
	"time"
)

// URL Store Data
var (
	urlStore = make(map[string]string)
	urlMu    sync.RWMutex
)

type urlReq struct {
	URL string `json:"url"`
}

type urlResp struct {
	ShortURL string `json:"short_url"`
}

// Rate Limiter Data
type clientInfo struct {
	count     int
	lastReset time.Time
}

var (
	clients   = make(map[string]*clientInfo)
	clientsMu sync.Mutex
)

// Random 6-character ID generator
func generateID() string {
	b := make([]byte, 4)
	rand.Read(b)
	return base64.RawURLEncoding.EncodeToString(b)[:6]
}

// Rate Limiter Middleware
func rateLimit(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		ip := r.RemoteAddr

		clientsMu.Lock()
		client, exists := clients[ip]

		if !exists || time.Since(client.lastReset) > time.Minute {
			clients[ip] = &clientInfo{count: 1, lastReset: time.Now()}
			clientsMu.Unlock()
			next(w, r)
			return
		}

		if client.count >= 5 {
			clientsMu.Unlock()
			w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(http.StatusTooManyRequests)
			json.NewEncoder(w).Encode(map[string]string{"error": "too many requests, try again later"})
			return
		}

		client.count++
		clientsMu.Unlock()

		next(w, r)
	}
}

// Shorten URL Handler
func shortenHandle(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var req urlReq
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil || req.URL == "" {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}

	id := generateID()

	urlMu.Lock()
	urlStore[id] = req.URL
	urlMu.Unlock()

	resp := urlResp{
		ShortURL: "http://localhost:8080/" + id,
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}

// Redirect Handler
func redirectHandle(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Path[1:]

	urlMu.RLock()
	originalURL, exists := urlStore[id]
	urlMu.RUnlock()

	if !exists {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "url not found"})
		return
	}

	http.Redirect(w, r, originalURL, http.StatusFound)
}

func main() {
	http.HandleFunc("/shorten", rateLimit(shortenHandle))
	http.HandleFunc("/", redirectHandle)

	println("Server is running on port 8080...")
	http.ListenAndServe(":8080", nil)
}
