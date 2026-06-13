# Student Profile Card using Type Hints and F-Strings

name = "Gopal Sharma"
age = 19
city = "Ajmer"
goal = "Software Engg"

student = {
    "name": name,
    "age": age,
    "city": city,
    "goal": goal
}


def create_profile(student_data: dict) -> str:
    return (
        f"Name : {student_data['name']}\n"
        f"Age  : {student_data['age']}\n"
        f"City : {student_data['city']}\n"
        f"Goal : {student_data['goal']}"
    )


print(create_profile(student))