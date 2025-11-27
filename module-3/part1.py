# This will prompt the user to enter the food charge.
food_cost = float(input("Enter the food amount: "))

# Calculate tip and sales tax amount
tip_amount = food_cost * 0.18       # 18% tip
tax_amount = food_cost * 0.07       # 7% sales tax

# Calculate total price including tip and sales tax
total_price = food_cost + tip_amount + tax_amount

# Display the results
print("\n----- Meal Cost Breakdown -----")
print(f"Food Charge:       ${food_cost:.2f}")
print(f"Tip (18%):         ${tip_amount:.2f}")
print(f"Sales Tax (7%):    ${tax_amount:.2f}")
print(f"Total Price:       ${total_price:.2f}")
