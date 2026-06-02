import pandas as pd

students = {
    "Name": ["Gopal", "Rahul", "Priya", "Aman"],
    "Math": [90, 78, 85, 70],
    "Science": [88, 80, 92, 75]
}

df = pd.DataFrame(students)

df["Total"] = df["Math"] + df["Science"]

print("Student Dashboard\n")

print(df)

print("\nAverage Total Marks:")
print(df["Total"].mean())

print("\nTop Performer:")
print(df.loc[df["Total"].idxmax()])