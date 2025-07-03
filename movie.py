# user wants to add movie data - movie title, director & year
def add_movieName():
    #print("TO ADD MOVIE DATA, ENTER 'yes' or 'no' to stop adding movies.")
    value =input("Do you want to add movie data? (yes/no): ").strip().lower()
    while value !="no":
        if value == "yes":
            title = input("Enter the movie name:")
            director = input("Enter the director's name:")
            year = input("Enter the realease year:")
            movies.append({
            "title": title,
            "director": director,
            "year": year
            })
            break
        

        



movies = [ ]





#display the list of movies

def display_movies():
    for movie in movies:
        print(f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")



#find the movies by title

def find_movie():
    value = input("Enter the movie title you want to search:").strip().lower()
    for movie in movies:
        title = movie['title'].lower()
        if title == value:
            print(f'Movie found: Title: {movie["title"]}, Director: {movie["director"]}, Year: {movie["year"]}')
        else:
            print("Movie not found.")
            break


selection = input("Enter 'add' to add a movie, 'list' to view all movies, 'find' to search for a movie, or 'quit' to quit:").strip().lower()
while selection != 'quit':
    if selection == "add":
        add_movieName()
        pass
    elif selection == "list":
        display_movies()
        pass
    elif selection == "find":
        find_movie()
        pass
    else:
        print('Unknown command. Please try again.')



