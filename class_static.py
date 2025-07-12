
class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def __average__(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0
    
newStudent = Student('Rolf', 'Mit')


class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
    
my_object = Foo()

my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I dont take parameters.')

another_object = Bar()

another_object.hi()
