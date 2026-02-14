# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from the user
number = int(input("Enter a number: "))

# Calling the function
output = factorial(number)

# Printing the result
print("Factorial of", number, "is:", output)
