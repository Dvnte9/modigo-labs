# The function below is meant to count how many times a specific character appears in a string using a for loop, but it isn't counting correctly. 
# Find the bug and fix it.

# Requirements

# Function name: count_character (do not rename it)
# Takes two parameters: text (a string) and target (a single character to count)
# Returns the number of times target appears in text, as an integer
# Comparison should be case-sensitive — "A" and "a" are different characters
# Examples

# count_character("banana", "a") → 3
# count_character("hello", "l") → 2
# count_character("hello", "z") → 0
# count_character("", "a") → 0
# Constraints

# text may be empty.
# target will always be a single character.
# text may not contain target at all.
# Note: Your solution will be tested against multiple cases, 
# including an empty string and a character that doesn't appear at all — look closely at what the loop is actually comparing.

def count_character(text, target):
    count = 0
    for char in text:
        if char == target:
            count += 1
    return count
