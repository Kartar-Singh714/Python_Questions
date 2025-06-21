# Product Inventory Manager
# Create a class Product with attributes name, price, and quantity.
# Add methods to purchase items (reduce stock) and check availability.


class Inventory_Manager:
    def __init__(self, name, price, quantity):
        self.name = name
        self. price = price
        self. quantity = quantity

    # def check_availablity(self):
    #     return self.quantity

    def purchase_items(self, count):
        count1 = int(count)
        updated_quantity = self.quantity-count1
        return updated_quantity

name = input("Enter the name of Product: ")
price = input("Enter the Price of Product: ")
quantity = int(input("Enter the quantities of Product: "))

product1 = Inventory_Manager(name, price, quantity)


print(f"The details of teh inventory are: \n Name: {product1.name} \n Price: {product1.price} Quantities left: {product1.quantity}")
count = input("Please enter the purchased items: ")
print(f"Updated Count = {product1.purchase_items(count)}")
