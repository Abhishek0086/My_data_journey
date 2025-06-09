age = 21
result = age >18 and age <65
print(result)

result = age < 18 or age >20
print(result)


default_name = " there "
name = input("What is your name? ")

user_name = name or default_name
print(f"Hello, {user_name}!")