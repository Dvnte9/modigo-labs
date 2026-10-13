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