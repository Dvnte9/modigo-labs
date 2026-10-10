# The function below is meant to take a list of coordinate tuples (some possibly repeated) and return how many distinct coordinates were visited. 
# It has a bug — find it and fix it.

# Requirements

# Function name: count_unique_coordinates (do not rename it)
# Takes one parameter: a list of tuples, coordinates, each shaped like (x, y)
# Returns the number of distinct coordinates as an integer
# If coordinates is empty, return 0
# Examples

# count_unique_coordinates([(0,0), (1,1), (0,0)]) → 2
# count_unique_coordinates([]) → 0
# count_unique_coordinates([(1,1), (1,1), (1,1)]) → 1
# count_unique_coordinates([(0,0), (1,0), (0,1)]) → 3
# Constraints

# The list may be empty.
# The list may contain the same coordinate repeated many times.
# Coordinates may include negative values.
# Note: Your solution will be tested against multiple cases, including an empty list and a list where every coordinate is identical.

def count_unique_coordinates(coordinates):
    return len(set(coordinates))
