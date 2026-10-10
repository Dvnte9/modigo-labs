# The function below is supposed to apply a discount to a price, defaulting to a 10% discount if no discount is specified. It has a bug — find it and fix it.

# Requirements

# Function name: apply_discount (do not rename it)
# Takes two parameters:
# price — a number (required, no default)
# discount_percent — a number, defaulting to 10
# Returns the price after subtracting the discount: price - (price * discount_percent / 100)
# Round the result to 2 decimal places
# Examples

# apply_discount(100) → 90.0 (default 10% discount)
# apply_discount(100, 20) → 80.0
# apply_discount(50, 0) → 50.0 (no discount)
# apply_discount(200, 50) → 100.0
# Constraints

# price must always be provided.
# discount_percent may be 0.
# Note: Your solution will be tested against multiple cases, 
# including using the default discount and passing 0 explicitly — pay attention to how the default is checked inside the function.

def apply_discount(price, discount_percent=10):
    return round(price - (price * discount_percent / 100), 2)
