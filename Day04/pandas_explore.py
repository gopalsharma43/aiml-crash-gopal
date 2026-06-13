# This program demonstrates basic Pandas operations.

import pandas as pd

students = {
    "name": [
        "Gopal",
        "Harsh",
        "Mishti",
        "Aman",
        "Neha",
        "Karan",
        "Riya",
        "Ankit",
        "Simran",
        "Vikas"
    ],

    "city": [
        "Ajmer",
        "Jaipur",
        "Jodhpur",
        "Ajmer",
        "Delhi",
        "Jaipur",
        "Delhi",
        "Ajmer",
        "Jodhpur",
        "Delhi"
    ],

    "math_score": [90, 78, 85, 60, 88, 92, 74, 81, 69, 95],

    "science_score": [85, 80, 90, 65, 84, 91, 70, 75, 72, 96],

    "english_score": [88, 76, 82, 70, 90, 89, 73, 80, 75, 94]
}

df = pd.DataFrame(students)

print("Student Dataset:\n")
print(df)

# Question 1
print("\nAverage score in each subject:")
print(df[["math_score", "science_score", "english_score"]].mean())

# Question 2
df["total_score"] = (
    df["math_score"] +
    df["science_score"] +
    df["english_score"]
)

top_student = df.loc[df["total_score"].idxmax()]

print("\nStudent with highest total score:")
print(top_student)

# Question 3
print("\nStudents from each city:")
print(df["city"].value_counts())

# Question 4
print("\nStudents with math score above 75:")
print(df[df["math_score"] > 75])

# Explore Section
print("\nTop 3 students by total score:")
print(df.nlargest(3, "total_score"))