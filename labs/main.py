def format_line_item(description, amount, tax_rate=7.5, currency="$"):
    # TODO: calculate the taxed total using tax_rate, round to 2 decimal places,# and return
    total = amount + (amount * tax_rate / 100)                         
    return f"{description}: {currency}{total}"