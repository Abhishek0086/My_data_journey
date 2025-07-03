my_student = {
    'name': 'Rolf Smith',
    'grades': [70,88,90,99]
}


def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


class student:
    def __init__(self, new_name, new_grades):#dunder function
        self.name = new_name
        self.grade =new_grades
    
    def average(self):
        return sum(self.grade) / len(self.grade)
    

studentOne = student('Rolf Smith', [70,88,90,99])