class Student:
    def __init__(self, name,age,rollno, school):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, age, rollno, school, salary):
        super().__init__(name,age,rollno,school)
        self.salary = salary
    
    @property
    def weekly_salary(self):
        return self.salary *37.5

student = WorkingStudent('Rolf', 25, '12345', 'MiT', 1000)
print(student.name)
student.marks.append(99)
print(student.weekly_salary)
student.marks.extend([87,67])
for marks in student.marks:
    print(marks)
    