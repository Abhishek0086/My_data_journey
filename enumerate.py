friends =  ['Rolf', 'ruth', 'Charlie', 'jen']
""" index = 0
for freinds in friends:
    print(f"{index} {freinds}")
    index += 1 """

counter = 0

for counter,friend in enumerate(friends,start = 1):
    print(f"{counter} {friend}")

print(list(enumerate(friends)))
print(dict(enumerate(friends)))

