def group_anagrams(words):
    # TODO: group words that are anagrams of each other, preserving first-seen order
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())