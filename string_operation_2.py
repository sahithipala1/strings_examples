"""
Time to join!

While normalizing your text, you noticed that one
 review had a particular structure. This review
 ends with the HTML tag <\i> and it has a lot  of
  commas in different places of the sentence.
  You decide to remove the tag from the end and use the strategy of
   splitting the string and joining it back again without the commas.

"""
movie = " the film,however,is all good<\i> "

movie_tag = movie.rstrip("<\i>")

print(movie_tag)

movie_no_comma = movie_tag.split(",")

print(movie_no_comma)

movie_join = " ".join(movie_no_comma)

print(movie_join)
