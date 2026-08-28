# Write a function that returns the sum of all even numbers in a list of integers.

# Requirements

# Function name: sum_even_numbers
# Takes one parameter: a list of integers, numbers
# Loop through the list and identify which numbers are even
# Return the total sum of only the even numbers, as an integer
# If there are no even numbers in the list, return 0
# The order of numbers in the input list does not affect the result — you're just summing, not tracking position
# Examples

# sum_even_numbers([1, 2, 3, 4, 5]) → 6 (2 + 4 = 6, odd numbers ignored)
# sum_even_numbers([1, 3, 5]) → 0 (no even numbers found)
# sum_even_numbers([]) → 0 (nothing to sum)
# sum_even_numbers([2, 4, 6, 8]) → 20 (all numbers are even)
# Constraints

# The list may be empty — your function must not crash, it should simply return 0.
# The list may contain negative numbers — remember that negative numbers can also be even (e.g., -4 is even).
# The list may contain 0 — remember 0 is considered even.
# Do not modify the input list; only read from it.
# Note: Your solution will be tested against multiple cases, including an empty list, a list with no even numbers, and a list containing negative numbers.

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_numbers([1,2,3,4,5]))
