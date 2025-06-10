art_friends = { "rolf", "bob", "jen" }
science_friends = {"jen","charlie"}

""" art_friends.add("lisa")
print(art_friends)
art_friends.remove("lisa")
print(art_friends) """

art_but_notscience = art_friends.difference(science_friends)
print(art_but_notscience)