class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def update_quantity(self, quantity):
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self):
        return sum([product.price * product.quantity for product in self.products])


p1 = Product('Apple', 1.5, 100)
p2 = Product('Banana', 0.5, 200)

inventory = Inventory()
inventory.add_product(p1)
inventory.add_product(p2)

print(p1.display_product_info())
print(p2.display_product_info())

print("Total inventory value: ", inventory.total_value())
