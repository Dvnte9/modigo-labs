# Below is a function meant to build a countdown list, counting down from a given starting number to 1. Some of the loop logic is missing — complete it.

# Requirements

# Function name: build_countdown (already defined — fill in the missing body)
# Takes one parameter: start, a positive integer
# Uses a for loop (with range()) to build the countdown
# Returns a list of integers counting down from start to 1, inclusive
# If start is 0, return an empty list
# Examples

# build_countdown(5) → [5, 4, 3, 2, 1]
# build_countdown(1) → [1]
# build_countdown(0) → []
# build_countdown(3) → [3, 2, 1]
# Constraints

# start will always be a non-negative integer.
# You must use range() inside a for loop — think about what step value counts downward.
# Note: Your solution will be tested against multiple cases, including start = 0 and start = 1.

def build_countdown(start):
    countdown = []
    # TODO: use a for loop with range() to count down from `start` to 1,
    # appending each number to `countdown`
    for n in range(start, 0, -1):
        countdown.append(n)
    return countdown
