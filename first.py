# --------------------
# -- String Methods --
# --------------------

# split() rsplit()

a = "I Love Python, Java, C, C++ and C#"

print(a.split())

b = "I-Love-Python-and-Java"

print(b.split("-"))

c = "I-Love-Python-and-Java-and-C++"

print(c.split("-", 3))

c = "I-Love-Python-and-Java-and-C++"

print(c.rsplit("-", 3))

# center()

e = "Python"
print(e.center(12))  # Spaces
print(e.center(12, '#'))  # Hashes
print(e.center(12, '@'))  # @

f = "I Love Python and C# Because Python And C# is Easy"
print(f.count("Python"))
print(f.count("C#"))

print(f.count("Python", 0, 15))
print(f.count("C#", 0, 33))

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# starswith()

g = "I Love Python"

print(g.startswith('I'))
print(g.startswith('S'))
print(g.startswith('P', 7, 12))

# endswith()

g = "I Love Python"

print(g.endswith("n"))
print(g.endswith("S"))
print(g.endswith("e", 2, 6))
