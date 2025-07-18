numbers = [0,1,2,3,4]
# doubled_numbers = []
# normal way

""" for number in numbers:
    doubled_numbers.append(number*2)
print(doubled_numbers)
 """
# list comprehension way
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)
# list comprehension with condition
# doubled_numbers = [number * 2 for number in numbers if number%2==0]
# print(doubled_numbers)
# list comprehension with condition and if-else
# doubled_numbers = [number * 2 if number % 2 == 0 else number for number in numbers]

""" friend_age = [ 23, 21 ,20 , 19]
age_groups = [f'My friens is {age} years old ,' for age in friend_age]
print(age_groups)
#in case we want names without brackets 
print("\n".join(age_groups))


names = ['Alice', 'Bob', 'Charlie']

lowercase_names = [name.lower() for name in names]
print(lowercase_names) """


""" friend = input("Enter your friend name:")
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
friends_lower = [f.lower() for f in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is your friend") """


""" ages = [23, 21, 20, 19]
odds =[age for age in ages if age % 2 == 1]
print(odds) """

friends = ['Rolf', 'ruth', 'Charlie', 'jen']
quests = ['jose', 'Bob', 'ROlf', 'Charlie', 'micheal']

""" friends_lower = set([f.lower() for f in friends])
quest_lower = set([q.lower() for q in quests]) """

""" print(friends_lower.intersection(quest_lower)) """

""" friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title()
    for name in quests
    if name.lower() in friends_lower
]
 """

friends_lower = {f.lower() for f in friends}
quests_lower = {q.lower() for q in quests}

common_friends = {name.title() for name in friends_lower.intersection(quests_lower)}
print(common_friends)

time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 10
}

print(long_timers)