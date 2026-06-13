import pandas as pd

employees = {
    "Name": ["Govind", "Gopal", "Priya", "Neha"],
    "Department": ["AI", "DevOps", "Data Science", "AI"],
    "Salary": [50000, 45000, 55000, 60000]
}

df = pd.DataFrame(employees)

print("Employee Data:\n")
print(df)

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Paid Employee:")
print(df.loc[df["Salary"].idxmax()])