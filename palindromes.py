"""
Palindromes

Next, you are committed to find any peculiarity in the words included in the movie review dataset.
 A palindrome is a sequence of characters which can be read the same backward as forward,
 for example: Madam or No lemon, no melon. You realize that there are some funny movie names that
 can have this characteristic. You want to make a list of all movie titles that are funny palindromes,
 but you will start by analyzing one example.

In python, you can also specify steps by using a third index.
If you don't specify the first or second index and the third one
is negative, it will return the characters jumping and backwards.

The text of a movie review for one example has been already
saved in the variable movie. You can use print(movie)
 to view the variable in the IPython Shell.



"""

movie = "oh my God! desserts I stressed was an ugly movie"

palindrome = movie[::-1]

print(palindrome)

# reverse the string

movie_1 = "123"
reverse = movie_1[::-1]
print(reverse)

# palindrome

dessert_2 = "Did Radar Noon desserts i stressed you got chocolates"

dessert_name = dessert_2[14:35]
print(dessert_name)

palindrome_1 = dessert_name[::-1]

if dessert_name == palindrome_1:
    print(palindrome_1)
else:
    print("not a palindrome")

















