art_friends = { "rolf", "bob", "jen" }
science_friends = {"jen","charlie"}

""" art_friends.add("lisa")
print(art_friends)
art_friends.remove("lisa")
print(art_friends) """

art_but_notscience = art_friends.difference(science_friends)
print(art_but_notscience)
science_but_notart = science_friends.difference(art_friends)
print(science_but_notart)


not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

friends_in_both = art_friends.intersection(science_friends)
print(friends_in_both)

friends_in_either = art_friends.union(science_friends)
print(friends_in_either)