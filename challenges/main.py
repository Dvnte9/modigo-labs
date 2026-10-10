def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    # TODO: loop through `text`, check each character (case-insensitively)
    # against `vowels`, and increment `count` when it matches
    return count