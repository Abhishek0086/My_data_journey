dictionary = {"name": "pluto", "type": "dog", "age": 5, "color": "brown"}
print(dictionary)

print(dictionary["type"])

dictionary["age"] = 6 # Update the age of the dog
print(dictionary)

collection = (
    {"name":"pluto"},
    {"name":"lisa"},
    {"name":"charlie"},
    {"name":"bob"},
    {"name":"jen"}
)

print(collection[0]["name"])