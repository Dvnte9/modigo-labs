# Cinema Ticket Pricing
# A cinema charges different prices depending on who's buying a ticket and when. Write a program that reads the customer's age and the day type, then works out the correct price.

# Instructions
# Write a program that:

# Asks for the customer's age using exactly this prompt: "Age: "
# Asks whether it's a weekday or weekend using exactly this prompt: "Day type (weekday/weekend): "
# Calculates the ticket price using these rules:
# Under 5: free — price is 0, regardless of day type.
# 5 to 12: 1500 on weekdays, 2000 on weekends.
# 13 to 59: 2500 on weekdays, 3500 on weekends.
# 60 and above: 1200 on weekdays, 1800 on weekends.
# Prints the result in exactly this format: "Price: {price}"
# Rules
# input() returns a string — convert age to an integer before comparing it.
# You must use if / elif / else — no dictionaries or lookup tables.
# Assume age will always be a valid non-negative integer, and day_type will always be exactly "weekday" or "weekend".
# Example
# If the program receives:

age = int(input("Age: "))
day_type = input("Day type (weekday/weekend): ")
day_type = day_type.strip().lower()
price = 0

if age <= 5:
    price = 0
elif age <= 12:
    if day_type == "weekday":
        price = 1500
    elif day_type == "weekend":
        price = 2000
elif age <= 59:
    if day_type == "weekday":
        price = 2500
    elif day_type == "weekend":
        price = 3500
else:
    if day_type == "weekday":
        price = 1200
    elif day_type == "weekend":
        price = 1800
print(f"Price: {price}")
