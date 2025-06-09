""" friends = ["Rolf", "Bob", "Anne"]
print(friends)
print(len(friends)) """

friends = [["rolf",24],
           ["bob", 30],
           ["anne", 27]
]
print(friends[0][1])  # Accessing the age of Rolf
print(friends[1][0])  # Accessing the name of Bob

friends.append(["lisa",21])
print(friends)

friends.remove(["anne", 27])
print(friends)