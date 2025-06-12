""" friend = 'Rolf'
user_name = input('Enter your name: ')

if user_name == friend:
    print('Hello,friend!')
else:
    print('Hello, stranger!') """

friends = ['Rolf', 'Anne', 'Charlie']
family = ['lisa']

user_name = input('Enter your name:')

if user_name in friends:
    print('Hello, friend!')
elif user_name in family:
    print('Hello,family member!')
else:
    print("Hello, stranger!")