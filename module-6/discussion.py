# Listing will beneficiaries
will_beneficiaries = ["Kim", "ye", "Ayo", "Aisha"]

will_beneficiaries.append("Charles")        # Add to the above list
will_beneficiaries.insert(5, "Scott")      # Inserts a new name at the end

print(will_beneficiaries)

will_beneficiaries[0] = "Tolu"   # Will update a name at the very beginning

print(will_beneficiaries)

will_beneficiaries.remove("Tolu")  # Remove Tolu as a beneficiary
will_beneficiaries.pop()             # Remove the last person
will_beneficiaries.pop(0)            # Remove the first person
del will_beneficiaries[1]            # Delete the second person

print(will_beneficiaries)

streamer = {"name": "Kai", "age": 26}

streamer["platform"] = "Twitch"   # Add new key-value pair
print(streamer)

# Update existing key-value pair
streamer["name"] = "Shank"
print(streamer)

streamer.pop("age")      # Remove by key
del streamer["name"]     # Delete 
streamer.clear()         # Remove all items

print(streamer)
