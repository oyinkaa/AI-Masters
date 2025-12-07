# Simulating a government shutdown
shutdown_active = True
days = 0

while shutdown_active:
    days += 1
    print(f"Day {days} of the government shutdown...")

    # Ask if an agreement has been reached
    response = input("Has Congress reached an agreement? (yes/no): ").lower()

    if response == "yes":
        shutdown_active = False
        print("The government shutdown is over.")
    else:
        print("No agreement yet. Shutdown continues.\n")