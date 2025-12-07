class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


print("What kind of Refrigerator")
name = input("What is the make of the refrigerator:\n")
price = float(input("Enter the price of the refrigerator:\n"))
quantity = int(input("How many refrigerators do you want?:\n"))

Refrigerator = ItemToPurchase(name, price, quantity)

print("\nWhat kind of Microwave")
name1 = input("What is the make of the microwave:\n")
price1 = float(input("Enter the price of the microwave:\n"))
quantity1 = int(input("How many microwave do you want?:\n"))

Microwave = ItemToPurchase(name1, price1, quantity1)

# TOTAL COST
print("\nTOTAL COST")
Refrigerator.print_item_cost()
Microwave.print_item_cost()

total = (Refrigerator.item_price * Refrigerator.item_quantity) + (Microwave.item_price * Microwave.item_quantity)
print(f"Total: ${total}")
