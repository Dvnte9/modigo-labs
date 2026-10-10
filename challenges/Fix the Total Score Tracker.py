# The function below is meant to take a list of round results and calculate each player's total score across all rounds. It has a bug — find it and fix it.

# Requirements

# Function name: total_scores (do not rename it)
# Takes one parameter: a list of dictionaries, rounds, where each dictionary maps player names to the points they scored that round (e.g., {"Ada": 5, "Bola": 3})
# Returns a dictionary mapping each player name to their total score summed across all rounds
# A player may not appear in every round — only sum the rounds they actually appear in
# Examples

# total_scores([{"Ada": 5, "Bola": 3}, {"Ada": 2, "Bola": 4}]) → {"Ada": 7, "Bola": 7}
# total_scores([{"Ada": 10}]) → {"Ada": 10}
# total_scores([]) → {}
# total_scores([{"Ada": 5}, {"Bola": 3}]) → {"Ada": 5, "Bola": 3} (each player only appeared once)
# Constraints

# rounds may be empty.
# A player may be missing from some rounds — only count rounds where they appear.
# There may be any number of players across the rounds.
# Note: Your solution will be tested against multiple cases, including a player who skips a round — look closely at what happens to a player's running total each time a new round is processed.

def total_scores(rounds):
    totals = {}
    for round_scores in rounds:
        for player, points in round_scores.items():
            if player in totals:
                totals[player] += points
            else:
                totals[player] = points
    return totals
