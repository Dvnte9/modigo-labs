def build_countdown(start):
    countdown = []
    # TODO: use a for loop with range() to count down from `start` to 1,
    # appending each number to `countdown`
    for n in range(start, 0, -1):
        countdown.append(n)
    return countdown