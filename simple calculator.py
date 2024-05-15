# Simple Calculator Program in Python

# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    return num1 / num2

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Print menu options
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform the selected operation
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid choice. Please choose a valid option (1/2/3/4).")
