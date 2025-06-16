""" cars = ['ok', 'ok', 'faulty', 'ok']

for status in cars:
    if status == 'faulty':
        print("Found faulty car, skipping it.")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!") """

""" my_friends = {
    'jose' : 6,
    'Rolf' : 12,
    'Anne' : 6
}

do_i_know = 'Anne'

if do_i_know in my_friends:
    print(f"Yes, I know {do_i_know}!") """


# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".


i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1  
    