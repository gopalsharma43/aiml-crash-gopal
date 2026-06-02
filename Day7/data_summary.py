import pandas as pd

students = {
    "Name": ["Gopal", "Govind", "Priya", "Aman", "Neha"],
    "Math": [90, 78, 85, 70, 95],
    "Science": [88, 80, 92, 75, 97]
}

df = pd.DataFrame(students)

print("Student Data:\n")
print(df)

print("\nAverage Marks:")

print("Math Average:", df["Math"].mean())
print("Science Average:", df["Science"].mean())

top_math = df.loc[df["Math"].idxmax()]

print("\nTop Student in Math:")
print(f"Name: {top_math['Name']}")
print(f"Math: {top_math['Math']}")
print(f"Science: {top_math['Science']}")

df["Total"] = df["Math"] + df["Science"]

print("\nData with Total Marks:")
print(df)