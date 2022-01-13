"""
Normalizing reviews

It's time to extract some important words present in your movie review dataset.
First, you need to normalize them and then, count their frequency.
Part of the normalization implies converting all the words to lowercase,
removing special characters and extracting the root of a word so you count the variants as one.

So imagine you have the following reviews: The movie surprises me very much
and Marvel movies always surprise their audience. If you count the word frequency,
 you will count surprises one time and surprise one time. However, the verb surprise
 appears in both and its frequency should be two.
 """

# Convert to lowercase and print the result
movie = " $i supposed that coming from mtv films i should expect no less$ ."

movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_sign = movie_lower.strip("$")
print(movie_no_sign)

# Split the string into substrings and print the result
movie_split = movie_no_sign.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][:-1]
print(word_root)
