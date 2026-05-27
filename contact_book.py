# This program searches for contacts in a mini contact book.

contacts = [
    {
        "name": "Gopal",
        "phone": "9876543210",
        "email": "gopal@gmail.com"
    },

    {
        "name": "Rahul",
        "phone": "9123456780",
        "email": "rahul@gmail.com"
    },

    {
        "name": "Mishti",
        "phone": "9988776655",
        "email": "priya@gmail.com"
    },

    {
        "name": "Aman",
        "phone": "9090909090",
        "email": "aman@gmail.com"
    },

    {
        "name": "Ani",
        "phone": "9012345678",
        "email": "neha@gmail.com"
    }
]


def find_contact(name):

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            return contact

    return "Contact not found."


search_name = input("Enter contact name to search: ")

result = find_contact(search_name)

print("\nSearch Result:")

print(result)