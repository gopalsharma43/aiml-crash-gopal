# This program checks whether a number is even, odd, or zero.

try:
    # int() converts user input into an integer.
    # If the user enters "abc", int() gives a ValueError because it cannot convert letters into numbers.
    
    number = int(input("Enter a number: "))

    if number == 0:
        print("The number is zero.")

    elif number % 2 == 0:
        print("The number is even.")

    else:
        print("The number is odd.")

except ValueError:
    print("Invalid input! Please enter a valid number.")