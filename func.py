def greet():
    """
    Prints the message "Hello World!" to the console.

    This function does not take any parameters and does not return any value.
    It simply prints the specified message to the console.

    Usage:
    >>> greet()
    Hello World!
    """
    name = input("Enter your name:")
    print(f'Hello, {name}.')

# greet()

car = [
    #    list of car attributes
    {"brand": "Ford", "model": "Mustang", "year": 1964, "mileage": 23000, "fuel_consummed": 460},
    {"brand": "Chevrolet", "model": "Camaro", "year": 1967, "mileage": 15000, "fuel_consummed": 300},
    {"brand": "Dodge", "model": "Charger", "year": 1970, "mileage": 12000, "fuel_consummed": 240},
    {"brand": "Porsche", "model": "911", "year": 1973, "mileage": 8000, "fuel_consummed": 160},
    {"brand": "Toyota", "model": "Corolla", "year": 1985, "mileage": 5000, "fuel_consummed": 100}
    ]




def calculte_mpg(car):
    mpg = car["mileage"] / car["fuel_consummed"]
    name = f'{car['brand']} {car['model']}'
    print(f'{name} does {mpg} miles per gallon.')

for cars in car:
    calculte_mpg(car)





    
    