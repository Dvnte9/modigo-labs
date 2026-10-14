# Task:

# Temperature Converter
# Your task is to write a Python program that converts a temperature given in Celsius to Fahrenheit.

# The formula for converting Celsius to Fahrenheit is: F = C * 9/5 + 32

# Input
# Your program will receive a single floating-point number representing the temperature in Celsius 
# from standard input (stdin).

# Output
# Your program should print the converted temperature in Fahrenheit to standard output (stdout). 
# The output should be a floating-point number, formatted to one decimal place.

# Constraints
# The input temperature will be a valid floating-point number.
# Example 1
# Input:

# code
# Copy
# 25.0
# Output:

# code
# Copy
# 77.0

# Read the Celsius temperature from standard input
# Remember to convert the input string to a number (float)
celsius_str = float(input())

# Convert Celsius to Fahrenheit using the formula: F = C * 9/5 + 32

# Store the result in a variable called 'fahrenheit'
fahrenheit = (celsius_str * 9/5 + 32) # Placeholder, replace with actual calculation

# Print the Fahrenheit temperature, formatted to one decimal place
print(f"{fahrenheit:.1f}")
