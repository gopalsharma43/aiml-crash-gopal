# This program demonstrates JSON read and write operations.

import json

students = [
    {
        "id": 101,
        "name": "Gopal",
        "course": "DevOps"
    },
    {
        "id": 102,
        "name": "Rishabh",
        "course": "DevOps"
    },
    {
        "id": 103,
        "name": "Priya",
        "course": "Data Science"
    }
]

# Write JSON

with open("Day4/students.json", "w") as file:
    json.dump(students, file, indent=4)

print("JSON file created successfully.\n")

# Read JSON

with open("Day4/students.json", "r") as file:
    loaded_students = json.load(file)

print("Student Records:\n")

for student in loaded_students:
    print(student)