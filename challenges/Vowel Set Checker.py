# Task:

# Below is a function meant to check whether a given word contains every one of the five vowels (a, e, i, o, u) 
# at least once. Some of the logic is missing — complete it.

# Requirements

# Function name: has_all_vowels (already defined — fill in the missing body)
# Takes one parameter: word, a string
# Treat the check as case-insensitive
# Returns True if all five vowels appear somewhere in word, False otherwise
# Use sets to compare the vowels found in the word against the full set of required vowels
# Examples

# has_all_vowels("education") → True
# has_all_vowels("hello") → False (missing a, i, u)
# has_all_vowels("SEQUOIA") → True (case-insensitive)
# has_all_vowels("") → False
# Constraints

# The word may be empty.
# The word may contain repeated vowels — that's fine, only presence matters, not count.
# The word may contain consonants, spaces, or punctuation, which should be ignored.
# Note: Your solution will be tested against multiple cases, including an empty string and a word with all vowels 
# repeated multiple times.

def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower() #treat as case-sensitive - lowercase 
    # TODO: build a set of vowels actually found in `word`,
    # then check if it contains all of `required`
    check = set() #creates an empty set
    for char in word: #loops through each character in the word
        if char in required: #checks if any of the character in 'word' is in 'required'
            check.add(char) #adds vowel characters to new set 
    return check == required #compares if all vowel characters - 'required' are available in 'check'
