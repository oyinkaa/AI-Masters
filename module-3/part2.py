# This will prompt the user for the current time in hours (0–23)
current_time = int(input("Enter the current time (0-23): "))

# This will prompt the user for the number of hours to wait for the alarm to go off
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time in 24-hour format
alarm_time = (current_time + hours_to_wait) % 24

# Display the result
print(f"\nWhen the alarm goes off, the time will be: {alarm_time}:00")
