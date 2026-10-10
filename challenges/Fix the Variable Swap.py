# The function below is supposed to take two values and return them swapped — the first value becomes the second, and the second becomes the first. 
# It has a bug — find it and fix it.

# Requirements

# Function name: swap_values (do not rename it)
# Takes two parameters: a and b
# Returns a tuple (new_a, new_b) where new_a equals the original b, and new_b equals the original a
# Examples

# swap_values(1, 2) → (2, 1)
# swap_values("hi", "bye") → ("bye", "hi")
# swap_values(5, 5) → (5, 5)
# Constraints

# a and b may be numbers or strings.
# a and b may already be equal to each other.
# Note: Your solution will be tested against multiple cases, 
#     including values of different types and equal values — think carefully about the order in which values get overwritten.

def swap_values(a, b):
    return b, a
print(swap_values(1, 2))
