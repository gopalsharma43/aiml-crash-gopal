# This program classifies students based on their scores.

students = [
    {"name": "Gopal", "score": 92},
    {"name": "Rahul", "score": 85},
    {"name": "Mishti", "score": 74},
    {"name": "Priya", "score": 63},
    {"name": "Harsh", "score": 50}
]


def classify(score):

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"


sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

print("Student Grades:\n")

for student in sorted_students:

    grade = classify(student["score"])

    print(f"{student['name']} scored {student['score']} and got Grade {grade}")