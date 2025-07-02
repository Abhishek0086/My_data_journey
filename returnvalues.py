cars = [ 
    {"brand": "Ford", "model": "Mustang", "year": 1964, "mileage": 23000, "fuel_consummed": 460},
    {"brand": "Chevrolet", "model": "Camaro", "year": 1967, "mileage": 15000, "fuel_consummed": 300},
    {"brand": "Dodge", "model": "Charger", "year": 1970, "mileage": 12000, "fuel_consummed": 240},
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consummed"]
    return mpg

def get_car_name(car):
    name = f'{car["brand"]} {car["model"]}'
    return name

def print_car_info(car):
    mpg = calculate_mpg(car)
    name = get_car_name(car)
    print(f'{name} does {mpg:.2f} miles per gallon.')


for car in cars:
    print_car_info(car)