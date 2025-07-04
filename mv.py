class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year


movie_data = [
    {        'name': 'The Matrix',
        'year': 1999}
    ,
    {'name': 'Inception', 'year': 2010},
]

for movie in movie_data:
    movie_instance = Movie(**movie)
    print(f'{movie_instance.name} was released in {movie_instance.year}.')
