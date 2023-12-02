# Strings
string = "WTF?"

# Integer

x = 4

# Float

y = 3.14

# Boolean

z = True

# List

a = ["True", True, 1, 1.0]

# Touple

b = ("True", True, 1, 1.0)

# Set

sets = {1, 3, 4, 4, 1, 2, 5}  # {1, 2, 3, 4, 5} as there is no duplication
print(sets)


# Dictionary

dictiomary = {"key": "value", "key2": "vales2"}


# Checking types is easy. Just use the type() function.

# print(type())

# We can use the dir() function to view all the functions of something.
temp = dir(str)
for r in temp:
    print(r)
