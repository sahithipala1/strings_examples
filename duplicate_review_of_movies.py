"""
Artificial reviews

While checking out the movie reviews in your dataset,
you realize that some of them show an atypical pattern.
Since you should only include true reviews in your analysis,
you decide to extract the suspicious ones that follow this pattern.
 You want to see if it is possible to artificially create reviews
 by using the first and last part of one example review and changing
 a keyword in the middle.

The text of two movie reviews has been already
saved in the variables movie1 and movie2. You
can use the print() function to view the variables in the IPython Shell.

Remember: The 1st character of a string has indexed 0.



"""

movie_1 = " the most significant tension of _election_ is the potential " \
          "relationship between a teacher and his student ."

movie_2 = " the most significant tension of _rushmore_ is the potential" \
          " relationship between a teacher and his student ."


first_part_review_movie_1 = movie_1[:32]

print(first_part_review_movie_1)

middle_part_movie_1 = movie_1[32:42]

print(middle_part_movie_1)







