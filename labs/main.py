def apply_discount(price, discount_percent=10):
    if not discount_percent:
        discount_percent = 0
    return round(price - (price * discount_percent / 100), 2)