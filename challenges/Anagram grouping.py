# Task:

# Write a function that groups words into clusters where every word in a cluster is an anagram of every other word 
# in it.

# Requirements

# Function name: group_anagrams
# Takes one parameter: words, a list of strings (all lowercase)
# Returns a list of lists, where each inner list contains words that are anagrams of each other
# Within each group, words should appear in the order they first appeared in words
# Groups themselves should appear in the order their first member first appeared in words
# If words is empty, return an empty list
# Examples

# group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) → [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# group_anagrams([]) → []
# group_anagrams(["abc"]) → [["abc"]]
# group_anagrams(["ab", "ba", "cd"]) → [["ab", "ba"], ["cd"]]
# Constraints

# words may be empty.
# A word may have no anagrams among the others, forming a group of one.
# Words consist only of lowercase letters.
# Note: Your solution will be tested against multiple cases, including an empty list, a single word with no anagrams, 
# and several distinct anagram groups mixed together.

def group_anagrams(words):
    # TODO: group words that are anagrams of each other, preserving first-seen order
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
