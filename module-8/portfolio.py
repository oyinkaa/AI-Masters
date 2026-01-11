# Portfolio Project: Online Shopping Cart 


# Step 1 Build the ItemToPurchase class

class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        # Format like: Bottled Water 10 @ $1 = $10
        item_total = self.item_price * self.item_quantity

        # Clean display (avoid 1.0 if user typed 1)
        price_display = int(self.item_price) if self.item_price.is_integer() else self.item_price
        total_display = int(item_total) if float(item_total).is_integer() else item_total

        print(f"{self.item_name} {self.item_quantity} @ ${price_display} = ${total_display}")

    def print_item_description(self):
        # Format like: Nike Romaleos: Volt color, Weightlifting shoes
        print(f"{self.item_name}: {self.item_description}")

# Step 4 Build the ShoppingCart class

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # list of ItemToPurchase objects

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                self.cart_items.pop(i)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        # Modify description, price, and/or quantity if found by name
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                # Update only if the new value is NOT default
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = float(item_to_modify.item_price)
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = int(item_to_modify.item_quantity)
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    # Step 6 Output shopping cart, output items descriptions

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if len(self.cart_items) == 0:
            print("\nSHOPPING CART IS EMPTY")
            return

        for item in self.cart_items:
            item.print_item_cost()

        total_cost = self.get_cost_of_cart()
        total_display = int(total_cost) if float(total_cost).is_integer() else total_cost
        print(f"\nTotal: ${total_display}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()

# Step 5 Implement the print_menu() function
def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("\nChoose an option:\n").strip().lower()

        if choice not in ("a", "r", "c", "i", "o", "q"):
            print("Invalid option. Please try again.")
            continue

        if choice == "q":
            break

        # Step 8 Add item to cart
        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))

            cart.add_item(ItemToPurchase(name, desc, price, qty))

        # Step 9  Remove item from cart
        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        # Step 10 Change item quantity
       
        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))

            # Hint from prompt: create a new ItemToPurchase object, then modify
            update_item = ItemToPurchase(item_name=name, item_quantity=qty)
            cart.modify_item(update_item)

        # Step 6 Output items' descriptions
        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions() 

        # =========================
        # Step 6 (Milestone 2)Output shopping cart

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total() 

# Step 7 Prompt user for name and date; create ShoppingCart; run menu

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
