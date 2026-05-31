# This program writes student data to a CSV file
# and then reads it back.

import csv

students = [
    ["Name", "Age", "City"],
    ["Gopal", 20, "Ajmer"],
    ["Apex", 21, "Jaipur"],
    ["Priya", 22, "Jodhpur"]
]

# Writing CSV

with open("Day4/students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(students)

print("CSV file created successfully.\n")

# Reading CSV

print("Reading CSV Data:\n")

with open("Day4/students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)