# Tiny Class with a Useful Method

class Course:

    def __init__(self, name: str, total_modules: int, completed_modules: int):
        self.name = name
        self.total_modules = total_modules
        self.completed_modules = completed_modules

    def progress(self) -> float:
        return (self.completed_modules / self.total_modules) * 100


course1 = Course("Python", 20, 12)
course2 = Course("Machine Learning", 15, 9)

print("Course Progress Report\n")

print(
    f"{course1.name}: "
    f"{course1.progress():.2f}% completed"
)

print(
    f"{course2.name}: "
    f"{course2.progress():.2f}% completed"
)