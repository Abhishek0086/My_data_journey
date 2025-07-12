#first class function

""" def greet():
    print("hello")

hello = greet
hello() """

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    "average":avg,
    "total":total,
    "top":top
}

students = [
    {"name": "Alice", "grades": (85, 90, 78)},
    {"name": "Bob", "grades": (88, 92, 80)},
    {"name": "Charlie", "grades": (90, 85, 88)},
    {"name": "David", "grades": (70, 75, 80)},
    {"name": "Eve", "grades": (95, 100, 98)}
]

for student in students:
    name =student["name"]
    grades = student["grades"]  

    print(f'student:{name}')
    operation = input("Enter operation (average, total, top): ").strip().lower()

    operation_function = operations[operation]
    print(operation_function(grades))
        