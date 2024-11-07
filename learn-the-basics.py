"""
    This script provides basic arithmetic operations and a greeting function.

    Functions:
        greet(name):
            Returns a greeting message for the given name.

        add(a, b):
            Returns the sum of two numbers.

        subtract(a, b):
            Returns the difference between two numbers.

        multiply(a, b):
            Returns the product of two numbers.

        divide(a, b):
            Returns the quotient of two numbers if the divisor is not zero, otherwise returns an error message.

    Main Execution:
        Prompts the user to enter their name and prints a greeting message.
        Prompts the user to enter two numbers and performs basic arithmetic operations (addition, subtraction, multiplication, division) on them, printing the results.
    """
def greet(name):
    return f"Hello, {name}!"
    # Return a greeting message for the given name

def add(a, b):
    return a + b
    # Return the sum of two numbers

def subtract(a, b):
    return a - b
    # Return the difference between two numbers

def multiply(a, b):
    return a * b
    # Return the product of two numbers

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    # Return the quotient of two numbers if the divisor is not zero, otherwise return an error message

if __name__ == "__main__":
    # Greeting
    name = input("Enter your name: ")
    print(greet(name))

    # Basic arithmetic operations
    print("Let's do some basic arithmetic operations.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
