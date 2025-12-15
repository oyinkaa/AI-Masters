# You will be prompted for number of books purchased
books = int(input("Enter the number of books purchased this month: "))

# Determine points to be given based on books purchased
if books == 0:
    points = 0
elif books == 2:
    points = 5
elif books == 4:
    points = 15
elif books == 6:
    points = 30
elif books >= 8:
    points = 60
else:
    points = 0

# Points will be outputted based on books purchased
print("Points awarded:", points)
