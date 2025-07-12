class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

class WorkingStudent(Student):
    def __init__(self, name,school, salary):
        super().__init__(name,school)
        self.salary = salary


rolf = WorkingStudent('Rolf', 'mit', 1000)
print(rolf.salary)
print(rolf.name)
print(rolf.school)

rolf.marks.append(90)
rolf.marks.append(88)
print(rolf.average())
