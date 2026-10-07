def count_items(items):
    # TODO: use a for loop to build a dictionary counting each item in `items`
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts