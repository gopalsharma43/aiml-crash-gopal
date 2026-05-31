# This program performs basic calculator operations using functions.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero."

    return a / b


try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")

    operation = input("Enter operation: ")

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    if operation in operations:

        result = operations[operation](num1, num2)

        print(f"\nResult: {result}")

    else:
        print("Invalid operation selected.")

except ValueError:
    print("Invalid input! Please enter valid numbers.")