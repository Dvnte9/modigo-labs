# The function below is supposed to take a list of numbers and return a new list where every number is doubled, without changing the original list. It has a bug — find it and fix it.

# Requirements

# Function name: double_values (do not rename it)
# Takes one parameter: numbers, a list of integers
# Uses a for loop to build the new list
# Returns a new list with every value doubled
# The original numbers list passed in must remain unchanged after the function runs
# Examples

# double_values([1, 2, 3]) → [2, 4, 6]
# double_values([]) → []
# double_values([0, -1, 5]) → [0, -2, 10]
# Constraints

# The list may be empty.
# The list may contain negative numbers or zero.
# After calling the function, the original list passed in must still have its original, undoubled values.
# Note: Your solution will be tested against multiple cases, and it will also check that the original input list was not modified.

def double_values(numbers):
    result = []
    for i in numbers:
        result.append(i*2)
    return result
