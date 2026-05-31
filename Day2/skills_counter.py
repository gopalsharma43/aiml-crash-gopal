# This program prints a numbered list of skills and their total count.

skills = [
    "Python",
    "Git",
    "GitHub",
    "Linux",
    "Docker",
    "Communication"
]

print("My Skills:\n")

for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")

print(f"\nTotal skills: {len(skills)}")