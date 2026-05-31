# This program demonstrates type hints and dataclasses.

from dataclasses import dataclass


@dataclass
class Employee:
    emp_id: int
    name: str
    department: str
    salary: float

    def annual_salary(self) -> float:
        return self.salary * 12


employee1 = Employee(101, "Gopal", "AI/ML", 50000)
employee2 = Employee(102, "Rahul", "DevOps", 45000)

print(employee1)
print(f"Annual Salary: ₹{employee1.annual_salary():,.2f}")

print()

print(employee2)
print(f"Annual Salary: ₹{employee2.annual_salary():,.2f}")