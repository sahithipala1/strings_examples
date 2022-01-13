"""
Split lines or split the line?

You are about to leave work when a colleague asks you to use your
string manipulation skills to help him. You need to read strings from a
file in a way that if the file contains strings on different lines, they are stored as
separate elements. He also wants you to break the strings into pieces if you see that they contain commas.
"""

file = "mtv films election, a high school comedy, is a current " \
       "example from there, director steven spielberg wastes " \
       "no time, taking us into the water on a midnight swim "

file_split = file.rsplit(",")

print(file_split)

for substring in file_split:
    substring_split = substring.split(",")
    print(substring_split)