import json


with open("Day7/settings.json", "r") as file:
    settings = json.load(file)

print("Current Settings:")
print(settings)

settings["theme"] = "light"

with open("Day7/settings.json", "w") as file:
    json.dump(settings, file, indent=4)

print("\nUpdated Settings:")
print(settings)