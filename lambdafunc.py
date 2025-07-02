#lambda function

#divide = lambda x, y: "Error: Division by zero is not allowed." if y == 0 else x / y

divide = lambda x,y: x/y
print(divide(10, 2))  # This will print 5.0
# print(lambda x, y: "Error: Division by zero is not allowed." if y == 0 else x / y)(10, 2)

def average(sequence):
    """
    Calculate the average of a sequence of numbers.

    Parameters:
    sequence (tuple): A tuple containing numeric values.

    Returns:
    float: The average of the numbers in the sequence.
    """
    return sum(sequence) / len(sequence)

students = [
    {"name": "Alice", "grades":(85, 90, 78)},
    {"name": "Bob", "grades":(88, 92, 80)},
    {"name": "Charlie", "grades":(90, 85, 88)},
    {"name": "David", "grades":(70, 75, 80)},
    {"name": "Eve", "grades":(95, 100, 98)}
]

for student in students:
    print(average(student["grades"]))