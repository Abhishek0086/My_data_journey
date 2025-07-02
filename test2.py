import config

# This line loads a set of 6 random numbers from the config file
lottery_numbers = config.lottery_numbers

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

top_player = players[0]  # start by saying "the top matching player is the first one"
 
for player in players:  # Go over each player
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # Calculate how many numbers they matched
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):  # If they matched more than the current top player...
        top_player = player  # Say this player is the new top player
 
# Calculate their winnings using the formula!
winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
 
print(f"{top_player['name']} won {winnings}.")