# The function below is meant to take a list of sentences and count the total number of words across all of them combined. It has a bug — find it and fix it.

# Requirements

# Function name: total_word_count (do not rename it)
# Takes one parameter: a list of strings, sentences
# Returns the total number of words across all sentences, as an integer
# Words in a sentence are separated by spaces
# Examples

# total_word_count(["hello world", "how are you"]) → 5
# total_word_count(["one"]) → 1
# total_word_count([]) → 0
# total_word_count(["", "hi there"]) → 2
# Constraints

# The list may be empty.
# A sentence in the list may be an empty string.
# Sentences may have different numbers of words.
# Note: Your solution will be tested against multiple cases, including an empty list and a list containing an empty string.

def total_word_count(sentences):
    total = 0
    for sentence in sentences:
        total += len(sentence.split())
    return total
