def total_word_count(sentences):
    total = 0
    for sentence in sentences:
        total += len(sentence.split())
    return total