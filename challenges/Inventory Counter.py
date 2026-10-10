# A small shop wants to know how many of each item they have in a stock list. Write a function that counts occurrences of each item.

# Requirements

# Function name: count_items
# Takes one parameter: a list of strings, items
# Uses a for loop to go through the list and build up counts
# Returns a dictionary where each key is an item name, and each value is how many times it appeared in items
# If items is empty, return an empty dictionary
# Examples

# count_items(["apple", "banana", "apple"]) → {"apple": 2, "banana": 1}
# count_items([]) → {}
# count_items(["egg", "egg", "egg"]) → {"egg": 3}
# count_items(["milk", "bread", "eggs"]) → {"milk": 1, "bread": 1, "eggs": 1}
# Constraints

# The list may be empty.
# The list may contain only one distinct item repeated many times.
# The list may contain no repeated items at all.
# Note: Your solution will be tested against multiple cases, including an empty list and a list with no repeats.

def count_items(items):
    # TODO: use a for loop to build a dictionary counting each item in `items`
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
