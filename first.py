# -----------------------------
# String Indexing & Slicing
# [1] All Data in Python ismObject
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Index ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# -----------------------------

# Indexing ( Access Single Item )

MyString = "I Love Python"

print(MyString[0])  # Index 0 => I
print(MyString[9])  # Index 9 => t

print(MyString[-1])  # Index -1 => First Character From End
print(MyString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(MyString[2:6])  # Love
print(MyString[7:11])  # Pyth

print(MyString[:10])  # If Start Is Not Here Will Start From 0 ( I Love Pyt )
print(MyString[5:])  # If Start Is Not Here Will Go The End~ ( e Python )

print(MyString[:])  # Full Data

print(MyString[0::1])  # Full Data
print(MyString[::1])  # Full Data

print(MyString[::2])
print(MyString[::3])

