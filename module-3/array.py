
# Scenario: Storing and updating boys' trip budget costs
# 0: Flights, 1: Hotel, 2: Food, 3: Transportation, 4: Activities
boys_trip_budget = [650, 550, 400, 350, 300]

# Update the activity budget (index 4)
boys_trip_budget[2] += 40 # Adding extra money for food cause a new restaurant just opened and got added to the itinerary

print("Updated Boys Trip Budget:", boys_trip_budget)