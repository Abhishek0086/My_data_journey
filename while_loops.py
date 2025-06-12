is_learning = True

while is_learning:
    print("you are learning python!")
    user_input = input("Are you still learning?")
    is_learning = user_input == "yes"
print("Goodbye!")