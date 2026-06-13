# This program demonstrates an inventory management system using OOP and CSV.

import csv


class Product:

    def __init__(self, name: str, price: float, quantity: int):

        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):

        return (
            f"{self.name} | "
            f"Price: ₹{self.price} | "
            f"Quantity: {self.quantity}"
        )


class Inventory:

    def __init__(self):

        self.products = []

    def add_product(self, product):

        self.products.append(product)

    def total_value(self) -> float:

        return sum(
            product.price * product.quantity
            for product in self.products
        )

    def find_product(self, name: str):

        for product in self.products:

            if product.name.lower() == name.lower():

                return product

        return None

    def save_to_csv(self, filename):

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(
                ["Name", "Price", "Quantity"]
            )

            for product in self.products:

                writer.writerow([
                    product.name,
                    product.price,
                    product.quantity
                ])

    def load_from_csv(self, filename):

        self.products = []

        with open(filename, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                product = Product(
                    row["Name"],
                    float(row["Price"]),
                    int(row["Quantity"])
                )

                self.products.append(product)


inventory = Inventory()

inventory.add_product(
    Product("Laptop", 50000, 5)
)

inventory.add_product(
    Product("Mouse", 800, 20)
)

inventory.add_product(
    Product("Keyboard", 1500, 10)
)

print("Inventory Value:")
print(f"₹{inventory.total_value()}")

print("\nSearch Result:")
print(inventory.find_product("mouse"))

inventory.save_to_csv(
    "Day4/inventory.csv"
)

print("\nInventory saved to CSV.")

inventory.load_from_csv(
    "Day4/inventory.csv"
)

print("\nLoaded Products:")

for product in inventory.products:

    print(product)