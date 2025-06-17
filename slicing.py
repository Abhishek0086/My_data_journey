friends = ['Rolf', 'Anne', 'Charlie', 'Bob', 'Jen']

print(friends[1:3])
print(friends[:])
print(friends[-1:1:-1])  # This will print an empty list because the start index is greater than the end index when stepping backwards.
print(friends[1:3:2])  # This will print ['Anne'] because it starts at index 1 and goes to index 3, stepping by 2.