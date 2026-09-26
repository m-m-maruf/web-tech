# import math

# # dy/dx = f(x, y)
# def f(x, y):
#     return x + y 


# # User Inputs
# print("=== Euler's Method ===")
# x0 = float(input("Enter initial x (x0): "))
# y0 = float(input("Enter initial y (y0): "))
# h = float(input("Enter step size (h): "))
# x_target = float(input("Enter target x (x_target): "))

# # Input & Boundary Error Handling
# if h <= 0:
#     print("Error: Step size h must be strictly positive (h > 0).")
# elif x_target < x0:
#     print("Error: Target x_target must be greater than or equal to x0.")
# else:
#     # steps, interval divisibility tolerance
#     n_exact = (x_target - x0) / h
#     n = round(n_exact)

#     if not math.isclose(n_exact, n, abs_tol=1e-7):
#         print("Error: (x_target - x0) is not evenly divisible by h.")
#     else:
#         # Maximum Iteration Safety Guard 
#         MAX_ITER = 100000
#         if n > MAX_ITER:
#             print(f"Error: Step count ({n}) exceeds safety limit ({MAX_ITER}).")
#         else:
#             x, y = x0, y0
#             print(f"\nInitial State: x = {x:.6f}, y = {y:.6f}")
#             print("-" * 55)

#             # Main Integration Loop 
#             diverged = False
#             for step in range(1, n + 1):
#                 slope = f(x, y)

#                 # Convergence/Divergence check
#                 if math.isnan(slope) or math.isinf(slope):
#                     print(
#                         f"Error: Derivative diverged/undefined at step {step}."
#                     )
#                     diverged = True
#                     break

#                 # Euler's formula
#                 y = y + h * slope
#                 x = x + h

#                 # intermediate steps (6 decimal places)
#                 print(
#                     f"Step {step:2d} | x = {x:.6f} | f(x,y) = {slope:.6f} | y = {y:.6f}"
#                 )

#             # Output
#             if not diverged and not (math.isnan(y) or math.isinf(y)):
#                 print("-" * 55)
#                 print(f"Approximate y({x_target:.6f}) = {y:.6f}\n")



# import math

# # dy/dx = f(x, y)
# def f(x, y):
#     return x + y  


# # User Inputs
# print("=== RK2: Heun's Method ===")
# x0 = float(input("Enter initial x (x0): "))
# y0 = float(input("Enter initial y (y0): "))
# h = float(input("Enter step size (h): "))
# x_target = float(input("Enter target x (x_target): "))

# # Error & Validation Handling 
# if h <= 0:
#     print("Error: Step size h must be strictly positive.")
# elif x_target < x0:
#     print("Error: Target x_target must be >= x0.")
# else:
#     n_exact = (x_target - x0) / h
#     n = round(n_exact)

#     if not math.isclose(n_exact, n, abs_tol=1e-7):
#         print("Error: Interval (x_target - x0) is not divisible by h.")
#     else:
#         MAX_ITER = 100000
#         if n > MAX_ITER:
#             print(f"Error: Required steps ({n}) exceed maximum limit.")
#         else:
#             x, y = x0, y0
#             print(f"\nInitial State: x = {x:.6f}, y = {y:.6f}")
#             print("-" * 65)

#             diverged = False
#             for step in range(1, n + 1):
#                 # Predictor slope (k1) and Corrector slope (k2)
#                 k1 = f(x, y)
#                 k2 = f(x + h, y + h * k1)

#                 if (
#                     math.isnan(k1)
#                     or math.isinf(k1)
#                     or math.isnan(k2)
#                     or math.isinf(k2)
#                 ):
#                     print(f"Error: Solution diverged at step {step}.")
#                     diverged = True
#                     break

#                 # solution formula
#                 y = y + h * (k1 + k2) / 2.0
#                 x = x + h

#                 # Print intermediate result
#                 print(
#                     f"Step {step:2d} | x = {x:.6f} | k1 = {k1:.6f} | k2 = {k2:.6f} | y = {y:.6f}"
#                 )

#             if not diverged and not (math.isnan(y) or math.isinf(y)):
#                 print("-" * 65)
#                 print(f"Approximate y({x_target:.6f}) = {y:.6f}\n")



# import math

# # dy/dx = f(x, y)
# def f(x, y):
#     return x + y  


# # User Inputs 
# print("=== RK2: Midpoint Method ===")
# x0 = float(input("Enter initial x (x0): "))
# y0 = float(input("Enter initial y (y0): "))
# h = float(input("Enter step size (h): "))
# x_target = float(input("Enter target x (x_target): "))

# # Error & Validation Handling
# if h <= 0:
#     print("Error: Step size h must be strictly positive.")
# elif x_target < x0:
#     print("Error: Target x_target must be >= x0.")
# else:
#     n_exact = (x_target - x0) / h
#     n = round(n_exact)

#     if not math.isclose(n_exact, n, abs_tol=1e-7):
#         print("Error: Interval (x_target - x0) is not divisible by h.")
#     else:
#         MAX_ITER = 100000
#         if n > MAX_ITER:
#             print(f"Error: Required steps ({n}) exceed maximum limit.")
#         else:
#             x, y = x0, y0
#             print(f"\nInitial State: x = {x:.6f}, y = {y:.6f}")
#             print("-" * 65)

#             diverged = False
#             for step in range(1, n + 1):
#                 # initial point (k1) and midpoint slope (k2)
#                 k1 = f(x, y)
#                 k2 = f(x + 0.5 * h, y + 0.5 * h * k1)

#                 if (
#                     math.isnan(k1)
#                     or math.isinf(k1)
#                     or math.isnan(k2)
#                     or math.isinf(k2)
#                 ):
#                     print(f"Error: Solution diverged at step {step}.")
#                     diverged = True
#                     break

#                 # solution (midpoint formula)
#                 y = y + h * k2
#                 x = x + h

#                 # Print intermediate result
#                 print(
#                     f"Step {step:2d} | x = {x:.6f} | k1 = {k1:.6f} | k2 = {k2:.6f} | y = {y:.6f}"
#                 )

#             if not diverged and not (math.isnan(y) or math.isinf(y)):
#                 print("-" * 65)
#                 print(f"Approximate y({x_target:.6f}) = {y:.6f}\n")




# import math

# # dy/dx = f(x, y)
# def f(x, y):
#     return x + y  


# # User Inputs
# print("=== RK2: Ralston's Method ===")
# x0 = float(input("Enter initial x (x0): "))
# y0 = float(input("Enter initial y (y0): "))
# h = float(input("Enter step size (h): "))
# x_target = float(input("Enter target x (x_target): "))

# # Error & Validation Handling
# if h <= 0:
#     print("Error: Step size h must be strictly positive.")
# elif x_target < x0:
#     print("Error: Target x_target must be >= x0.")
# else:
#     n_exact = (x_target - x0) / h
#     n = round(n_exact)

#     if not math.isclose(n_exact, n, abs_tol=1e-7):
#         print("Error: Interval (x_target - x0) is not divisible by h.")
#     else:
#         MAX_ITER = 100000
#         if n > MAX_ITER:
#             print(f"Error: Required steps ({n}) exceed maximum limit.")
#         else:
#             x, y = x0, y0
#             print(f"\nInitial State: x = {x:.6f}, y = {y:.6f}")
#             print("-" * 65)

#             diverged = False
#             for step in range(1, n + 1):
#                 # k1 at initial point, k2 at 2/3 of step size
#                 k1 = f(x, y)
#                 k2 = f(x + (2.0 / 3.0) * h, y + (2.0 / 3.0) * h * k1)

#                 if (
#                     math.isnan(k1)
#                     or math.isinf(k1)
#                     or math.isnan(k2)
#                     or math.isinf(k2)
#                 ):
#                     print(f"Error: Solution diverged at step {step}.")
#                     diverged = True
#                     break

#                 # Ralston's weighted formula
#                 y = y + h * (k1 / 4.0 + (3.0 * k2) / 4.0)
#                 x = x + h

#                 # Print intermediate result
#                 print(
#                     f"Step {step:2d} | x = {x:.6f} | k1 = {k1:.6f} | k2 = {k2:.6f} | y = {y:.6f}"
#                 )

#             if not diverged and not (math.isnan(y) or math.isinf(y)):
#                 print("-" * 65)
#                 print(f"Approximate y({x_target:.6f}) = {y:.6f}\n")
# k1 = f(x, y)
# k2 = f(x + (3.0 / 4.0) * h, y + (3.0 / 4.0) * h * k1)
# y = y + h * (k1 / 3.0 + (2.0 * k2) / 3.0)
# x = x + h
              

# import math

# # dy/dx = f(x, y)
# def f(x, y):
#     return x + y  


# # User Inputs
# print("=== RK4 Method ===")
# x0 = float(input("Enter initial x (x0): "))
# y0 = float(input("Enter initial y (y0): "))
# h = float(input("Enter step size (h): "))
# x_target = float(input("Enter target x (x_target): "))

# # Error & Validation Handling
# if h <= 0:
#     print("Error: Step size h must be strictly positive.")
# elif x_target < x0:
#     print("Error: Target x_target must be >= x0.")
# else:
#     n_exact = (x_target - x0) / h
#     n = round(n_exact)

#     if not math.isclose(n_exact, n, abs_tol=1e-7):
#         print("Error: Interval (x_target - x0) is not divisible by h.")
#     else:
#         MAX_ITER = 100000
#         if n > MAX_ITER:
#             print(f"Error: Required steps ({n}) exceed maximum limit.")
#         else:
#             x, y = x0, y0
#             print(f"\nInitial State: x = {x:.6f}, y = {y:.6f}")
#             print("-" * 85)

#             diverged = False
#             for step in range(1, n + 1):
#                 # 4 stage slopes
#                 k1 = f(x, y)
#                 k2 = f(x + 0.5 * h, y + 0.5 * h * k1)
#                 k3 = f(x + 0.5 * h, y + 0.5 * h * k2)
#                 k4 = f(x + h, y + h * k3)

#                 # Check divergence
#                 if any(math.isnan(k) or math.isinf(k) for k in [k1, k2, k3, k4]):
#                     print(f"Error: Solution diverged at step {step}.")
#                     diverged = True
#                     break

#                 # RK4 formula
#                 y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
#                 x = x + h

#                 # Print intermediate result
#                 print(
#                     f"Step {step:2d} | x = {x:.6f} | k1={k1:.6f} | k2={k2:.6f} | k3={k3:.6f} | k4={k4:.6f} | y = {y:.6f}"
#                 )

#             if not diverged and not (math.isnan(y) or math.isinf(y)):
#                 print("-" * 85)
#                 print(f"Approximate y({x_target:.6f}) = {y:.6f}\n")




# import math

# # Define the differential equation dy/dx = f(x, y)
# # Update this function based on the specific exam problem
# def f(x, y):
#     return x + y 


# def euler_method(x0, y0, h, x_target):
#     print("\n--- Euler's Method ---")
    
#     # 1. Input & Boundary Validation
#     if h <= 0:
#         return "Error: Step size h must be strictly positive."
#     if x_target < x0:
#         return "Error: Target x must be >= initial x0."
        
#     # 2. Compute steps and check interval divisibility tolerance
#     n_exact = (x_target - x0) / h
#     n = round(n_exact)
#     if not math.isclose(n_exact, n, abs_tol=1e-7):
#         return "Error: Interval length must be evenly divisible by h."
        
#     # 3. Maximum Iteration Safety Guard
#     MAX_ITER = 100000
#     if n > MAX_ITER:
#         return f"Error: Step count ({n}) exceeds safety limit."

#     x, y = x0, y0
#     print(f"Init : x = {x:.6f}, y = {y:.6f}")
    
#     # 4. Main Integration Loop
#     for step in range(1, n + 1):
#         slope = f(x, y)
        
#         # 5. Convergence/Divergence check
#         if math.isnan(slope) or math.isinf(slope):
#             return f"Error: Derivative diverged at step {step}."

#         # Advance solution using Euler's formula
#         y = y + h * slope
#         x = x + h
        
#         # Print intermediate results to consistent 6 decimal places
#         print(f"Step {step}: x = {x:.6f} | f(x,y) = {slope:.6f} | y = {y:.6f}")
        
#     print(f"Approximate y({x_target:.6f}) = {y:.6f}")
#     return y


# def heun_method(x0, y0, h, x_target):
#     print("\n--- RK2: Heun's Method ---")
    
#     if h <= 0 or x_target < x0:
#         return "Error: Invalid boundaries or step size."
        
#     n = round((x_target - x0) / h)
#     if not math.isclose((x_target - x0) / h, n, abs_tol=1e-7):
#         return "Error: Interval not divisible by h."
        
#     if n > 100000:
#         return "Error: Exceeded maximum iteration limit."

#     x, y = x0, y0
#     print(f"Init : x = {x:.6f}, y = {y:.6f}")
    
#     for step in range(1, n + 1):
#         # Calculate predictor and corrector slopes
#         k1 = f(x, y)
#         k2 = f(x + h, y + h * k1)
        
#         if any(math.isnan(k) or math.isinf(k) for k in [k1, k2]):
#             return f"Error: Solution diverged at step {step}."

#         # Advance solution using average slope
#         y = y + h * (k1 + k2) / 2.0
#         x = x + h
        
#         print(f"Step {step}: x = {x:.6f} | k1 = {k1:.6f} | k2 = {k2:.6f} | y = {y:.6f}")
        
#     print(f"Approximate y({x_target:.6f}) = {y:.6f}")
#     return y


# def midpoint_method(x0, y0, h, x_target):
#     print("\n--- RK2: Midpoint Method ---")
    
#     if h <= 0 or x_target < x0:
#         return "Error: Invalid boundaries or step size."
        
#     n = round((x_target - x0) / h)
#     if not math.isclose((x_target - x0) / h, n, abs_tol=1e-7):
#         return "Error: Interval not divisible by h."
        
#     if n > 100000:
#         return "Error: Exceeded maximum iteration limit."

#     x, y = x0, y0
#     print(f"Init : x = {x:.6f}, y = {y:.6f}")
    
#     for step in range(1, n + 1):
#         # Calculate slope at initial point and midpoint
#         k1 = f(x, y)
#         k2 = f(x + 0.5 * h, y + 0.5 * h * k1)
        
#         if any(math.isnan(k) or math.isinf(k) for k in [k1, k2]):
#             return f"Error: Solution diverged at step {step}."

#         # Advance solution using midpoint slope
#         y = y + h * k2
#         x = x + h
        
#         print(f"Step {step}: x = {x:.6f} | k1 = {k1:.6f} | k2 = {k2:.6f} | y = {y:.6f}")
        
#     print(f"Approximate y({x_target:.6f}) = {y:.6f}")
#     return y


# def ralston_method(x0, y0, h, x_target):
#     print("\n--- RK2: Ralston's Method ---")
    
#     if h <= 0 or x_target < x0:
#         return "Error: Invalid boundaries or step size."
        
#     n = round((x_target - x0) / h)
#     if not math.isclose((x_target - x0) / h, n, abs_tol=1e-7):
#         return "Error: Interval not divisible by h."
        
#     if n > 100000:
#         return "Error: Exceeded maximum iteration limit."

#     x, y = x0, y0
#     print(f"Init : x = {x:.6f}, y = {y:.6f}")
    
#     for step in range(1, n + 1):
#         # Calculate slopes at initial point and 2/3 interval
#         k1 = f(x, y)
#         k2 = f(x + (2.0 / 3.0) * h, y + (2.0 / 3.0) * h * k1)
        
#         if any(math.isnan(k) or math.isinf(k) for k in [k1, k2]):
#             return f"Error: Solution diverged at step {step}."

#         # Advance solution using Ralston's weighted formula
#         y = y + h * (k1 / 4.0 + 3.0 * k2 / 4.0)
#         x = x + h
        
#         print(f"Step {step}: x = {x:.6f} | k1 = {k1:.6f} | k2 = {k2:.6f} | y = {y:.6f}")
        
#     print(f"Approximate y({x_target:.6f}) = {y:.6f}")
#     return y


# def rk4_method(x0, y0, h, x_target):
#     print("\n--- Runge-Kutta 4th Order (RK4) ---")
    
#     if h <= 0 or x_target < x0:
#         return "Error: Invalid boundaries or step size."
        
#     n = round((x_target - x0) / h)
#     if not math.isclose((x_target - x0) / h, n, abs_tol=1e-7):
#         return "Error: Interval not divisible by h."
        
#     if n > 100000:
#         return "Error: Exceeded maximum iteration limit."

#     x, y = x0, y0
#     print(f"Init : x = {x:.6f}, y = {y:.6f}")
    
#     for step in range(1, n + 1):
#         # Calculate the 4 stage slopes for RK4
#         k1 = f(x, y)
#         k2 = f(x + 0.5 * h, y + 0.5 * h * k1)
#         k3 = f(x + 0.5 * h, y + 0.5 * h * k2)
#         k4 = f(x + h, y + h * k3)
        
#         if any(math.isnan(k) or math.isinf(k) for k in [k1, k2, k3, k4]):
#             return f"Error: Solution diverged at step {step}."

#         # Advance solution with weighted average
#         y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
#         x = x + h
        
#         print(f"Step {step}: x={x:.6f} | k1={k1:.6f} | k2={k2:.6f} | k3={k3:.6f} | k4={k4:.6f} | y={y:.6f}")
        
#     print(f"Approximate y({x_target:.6f}) = {y:.6f}")
#     return y


# # ==========================================
# # User Input Section (Runs immediately)
# # ==========================================
# print("=== ODE Numerical Solver Setup ===")
# user_x0 = float(input("Enter initial x (x0): "))
# user_y0 = float(input("Enter initial y (y0): "))
# user_h = float(input("Enter step size (h): "))
# user_target = float(input("Enter target x (x_target): "))

# # Execute all methods sequentially to demonstrate results
# euler_method(user_x0, user_y0, user_h, user_target)
# heun_method(user_x0, user_y0, user_h, user_target)
# midpoint_method(user_x0, user_y0, user_h, user_target)
# ralston_method(user_x0, user_y0, user_h, user_target)
# rk4_method(user_x0, user_y0, user_h, user_target)
