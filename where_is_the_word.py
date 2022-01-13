movies = "137    heck , jackie doesn't even have enough money f..."
print(movies.index("jackie", 1, 43))
print(movies)
for movie in movies:
    try:
        # Find the first occurrence of word
        print(movie.index("money", 12, -1))
    except ValueError:
        print("substring not found")
