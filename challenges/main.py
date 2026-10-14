# Read the Celsius temperature from standard input
# Remember to convert the input string to a number (float)
celsius_str = float(input())

# Convert Celsius to Fahrenheit using the formula: F = C * 9/5 + 32

# Store the result in a variable called 'fahrenheit'
fahrenheit = (celsius_str * 9/5 + 32) # Placeholder, replace with actual calculation

# Print the Fahrenheit temperature, formatted to one decimal place
print(f"{fahrenheit:.1f}")