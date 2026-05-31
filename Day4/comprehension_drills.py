# This program demonstrates list comprehensions in Python.

# Task 1
numbers = list(range(1, 21))
divisible_by_3 = [num for num in numbers if num % 3 == 0]

print("Numbers divisible by 3:")
print(divisible_by_3)


# Task 2
words = ["python", "code", "developer", "git", "github", "docker"]

long_words = [word.title() for word in words if len(word) > 4]

print("\nWords longer than 4 characters:")
print(long_words)


# Task 3
celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("\nTemperatures in Fahrenheit:")
print(fahrenheit)


# Task 4
nested = [[1, 2], [3, 4], [5, 6], [7, 8]]

flattened = [num for sublist in nested for num in sublist]

print("\nFlattened List:")
print(flattened)


# Explore Section

# Dict Comprehension
square_dict = {num: num**2 for num in range(1, 6)}

# Set Comprehension
square_set = {num**2 for num in range(1, 6)}

print("\nDictionary Comprehension:")
print(square_dict)

print("\nSet Comprehension:")
print(square_set)