# Gas prices for previous and current administration (6 months each)
previous_admin_prices = [3.50, 3.40, 3.45, 3.38, 3.30, 3.35]
current_admin_prices = [3.32, 3.28, 3.31, 3.29, 3.27, 3.25]

print("Gas Price Comparison Over 6 Months:")

for i in range(6):
    print(f"Month {i+1}: Previous = ${previous_admin_prices[i]}, Current = ${current_admin_prices[i]}")
