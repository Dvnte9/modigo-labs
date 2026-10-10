# Below is a function that's meant to count how many vowels (a, e, i, o, u) appear in a given string. Some of the logic is missing — complete it.

# Requirements

# Function name: count_vowels (already defined for you — fill in the missing body)
# Takes one parameter: a string, text
# Count only the letters a, e, i, o, u — treat uppercase and lowercase the same way (both "a" and "A" should count)
# Ignore all other characters: consonants, digits, punctuation, and spaces should not be counted
# Return the total count as an integer
# Examples

# count_vowels("hello") → 2 (the letters "e" and "o")
# count_vowels("SKY") → 0 (no vowels, "Y" is not counted as a vowel here)
# count_vowels("") → 0 (empty string has nothing to count)
# count_vowels("Education") → 5 (E, u, a, i, o — case doesn't matter)
# Constraints

# The string may be empty.
# The string may contain numbers, punctuation, or spaces — these should simply be skipped, not cause an error.
# The string may be entirely uppercase, entirely lowercase, or mixed case.
# You should loop through each character in text one at a time and check it against the vowel set.
# Note: Your solution will be tested against multiple cases, including an empty string, an all-uppercase string, 
# and a string with mixed letters, numbers, and punctuation.

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    # TODO: loop through `text`, check each character (case-insensitively)
    # against `vowels`, and increment `count` when it matches
    return count
