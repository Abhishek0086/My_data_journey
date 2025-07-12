#default value for a function parameter
def add(x,y=3):
    total = x+y
    return total

# print(add(5))
print(add(5, 10))  # This will print 15
#named arguments
print(add(y=3,x=4))  # This will print 7
#print(add(x=3, 4)) # This will raise a TypeError because positional argument follows named argument
# print(add(3, y=4))  # This will print 7


print(1, 2, 3, sep='-', end='!')
# This will print "1-2-3!" with '-' as the separator and '!'