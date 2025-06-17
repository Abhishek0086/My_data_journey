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

friend_age = [ 23, 21 ,20 , 19]
age_groups = [f'My friens is {age} years old ,' for age in friend_age]
print(age_groups)
