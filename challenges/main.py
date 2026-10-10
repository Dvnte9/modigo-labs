def replace_first(items, new_value):
    if not items:
        return ()
    return (new_value,) + items[1:]
print(replace_first((1, 2, 3), 9))