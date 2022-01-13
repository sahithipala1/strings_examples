my_string = "Where's Waldo?"
print(my_string.find("Waldo"))
print(my_string.find("Where's"))

try:
    my_string.index("Wenda")
except ValueError:
    print("not found")

# find substrings
s = "hello world"
print(s.find("world"))

