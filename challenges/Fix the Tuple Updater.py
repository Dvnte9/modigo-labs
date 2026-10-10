# The function below should return a new tuple where the first element has been replaced by a new value. It crashes instead. Find the bug and fix it.

# Requirements

# Function name: replace_first (do not rename it)
# Takes two parameters: items (a tuple) and new_value (any value)
# Returns a new tuple with the first element replaced by new_value and every other element unchanged
# If items is empty, return an empty tuple
# Examples

# replace_first((1, 2, 3), 9) → (9, 2, 3)
# replace_first(("a",), "z") → ("z",)
# replace_first((), 5) → ()
# Constraints

# items may be empty.
# items may contain only one element.
# Elements may be of any type.
# Note: Your solution will be tested against multiple cases, including an empty tuple and a single-element tuple. Remember that tuples are immutable.

def replace_first(items, new_value):
    if not items:
        return ()
    return (new_value,) + items[1:]
