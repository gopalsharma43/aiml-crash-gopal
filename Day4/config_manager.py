# This program manages application configuration using JSON.

import json


def save_config(config, filename):

    with open(filename, "w") as file:

        json.dump(config, file, indent=4)


def load_config(filename):

    with open(filename, "r") as file:

        return json.load(file)


def update_config(filename, key, value):

    config = load_config(filename)

    config[key] = value

    save_config(config, filename)


config_data = {
    "theme": "dark",
    "language": "English",
    "auto_save": True
}

filename = "Day4/config.json"

save_config(config_data, filename)

print("Initial Configuration:")
print(load_config(filename))

update_config(
    filename,
    "theme",
    "light"
)

print("\nUpdated Configuration:")
print(load_config(filename))