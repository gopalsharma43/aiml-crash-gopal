# This program reads student marks from a CSV file,
# calculates averages and grades, then writes results to a new CSV.

import csv

students = [
    ["name", "math", "science", "english"],
    ["Gopal", 90, 85, 88],
    ["Rahul", 78, 80, 76],
    ["Priya", 95, 92, 90]
]

# Create students.csv
with open("Day4/students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("students.csv created.")

results = []

with open("Day4/students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        math = int(row["math"])
        science = int(row["science"])
        english = int(row["english"])

        average = (math + science + english) / 3

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        results.append({
            "name": row["name"],
            "average": round(average, 2),
            "grade": grade
        })

# Create results.csv
with open("Day4/results.csv", "w", newline="") as file:

    fieldnames = ["name", "average", "grade"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(results)

print("results.csv created.")

print("\nResults:")
for result in results:
    print(result)