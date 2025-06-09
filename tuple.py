short_tuple = "Rolf","Bob"
a_bit_clearer = ("Rolf", "Bob")

friends = ("Rolf", "Bob", "Anne")
# friends.append("jen")# This will raise an AttributeError because tuples do not have an append method
#tuple is immutable, meaning you cannot change its contents after creation.

friends = friends + ("Jen",)  # Correct way to add an element to a tuple
print(friends)