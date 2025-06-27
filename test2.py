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

for name, numbers in enumerate(players.items()):
    print(f'{name} won {100 ** len(numbers.intersection(lottery_numbers))}')