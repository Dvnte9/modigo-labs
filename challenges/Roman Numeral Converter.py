# Task:

# Write a function from scratch that converts a positive integer into a Roman numeral string.

# Requirements

# Function name: to_roman
# Takes one parameter: number, an integer between 1 and 3999 inclusive
# Returns the Roman numeral as a string, using uppercase letters
# The seven basic symbols are: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Subtractive forms must be used where applicable: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900 
# — for example, 4 is "IV", never "IIII"
# Examples

# to_roman(1) → "I"
# to_roman(4) → "IV"
# to_roman(14) → "XIV"
# to_roman(1994) → "MCMXCIV"
# to_roman(3999) → "MMMCMXCIX"
# Constraints

# number is always between 1 and 3999 inclusive.
# Every subtractive case (4, 9, 40, 90, 400, 900 and numbers containing them) must be handled, 
# not just the basic symbols.
# Note: Your solution will be tested against multiple cases, 
# including the smallest and largest valid inputs and several numbers requiring subtractive notation.

# No starter code provided — write the full function yourself.
# Function name: to_roman
# Parameter: number (1 to 3999)
# Must return: the Roman numeral as a string

def to_roman(number):
    values = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, 
        "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1,
    }
    result = ""
    for symbol, value in values.items():
        while number >= value:
            result += symbol
            number -= value
    return result
