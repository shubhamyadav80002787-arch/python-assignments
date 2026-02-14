import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Perform calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)      # log base e
sine_value = math.sin(num)       # input in radians

# 3. Display the results
print("\nResults:")
print("Square root:", square_root)
print("Natural logarithm (log base e):", natural_log)
print("Sine (in radians):", sine_value)
