
class Student:
    def __init__(self,name):
        self.name = name


movies = ['matrix', 'Finding Nemo']

print(movies.__class__)  # <class 'list'>   




class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index):
        return self.cars[index]
    def __repr__(self):
        return f'<Garage with {self.cars}>'
    def __str__(self):
        return f'Garage with  {len(self)} cars:'
    

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focas')

print(ford[0]) #Garage.__getitems__(ford, 0)  # Fiesta
