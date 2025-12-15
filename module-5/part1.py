# Get the number of years from the user

numberofyears = int(input("Number of years with rainfall: "))

totalrainfall = 0
totalmonths = 0

# Outer loop for each year
for year in range(1, numberofyears + 1):
    print(f"\nYear {numberofyears}")
    
    # Inner loop for each month runs from 1 -12
    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for month {month}: "))
        totalrainfall += rainfall
        totalmonths += 1

# Find the average amount of rain that falls each month by dividing the totalrainfall by the totalmonths    
average_rainfall = totalrainfall / totalmonths

# Results
print("\nRainfall Summary")
print("Total months:", totalmonths)
print("Total rainfall:", totalrainfall, "inches")
print("Average rainfall per month:", average_rainfall, "inches")
