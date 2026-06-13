# This program is a number guessing game.

import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:

    try:

        guess = int(input("Enter your guess: "))

        attempts += 1

        if guess == secret_number:

            print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
            break

        elif guess < secret_number:

            print("Too low.\n")

        else:

            print("Too high.\n")

    except ValueError:

        print("Invalid input! Please enter a number.\n")

else:

    print(f"\nGame Over! The correct number was {secret_number}.")