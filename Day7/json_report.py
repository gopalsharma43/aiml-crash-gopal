import json

with open("Day7/learner.json", "r") as file:
    learner = json.load(file)

skills_upper = [skill.upper() for skill in learner["skills"]]

print("=== Learner Report ===\n")

print(f"Name  : {learner['name']}")
print(f"Role  : {learner['role']}")
print(f"Skills: {', '.join(skills_upper)}")