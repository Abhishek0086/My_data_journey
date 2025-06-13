currencies = 0.8, 1.2

usd, eur = currencies

friends = [('Rolf',25), ('Anne',23), ('Charlie',30)]

for name, age in friends:
    print(f'{name} is {age} years old')

friend_ages = {'rolf':25, 'anne':23, 'charlie':30}

for age in friend_ages.values():
    print(age)
for name,age in friend_ages.items():
    print(f'{name} is {age} years old')