#Strings: ordered, immutable, text representation

print("String can be initialized with either double(\") or single quotes(')")
my_string = "Hello world!"
print(my_string)

print("\nIn order to have quotes show up in the string, an escape character might be needed in order to not have it close"
      " out the string early.")
my_string = 'I\'m learning Python.'
print(my_string)

print("\nSometimes triple double quotes(""\") are used for multi-line sentences. They can also be used for multi-line "
      "comments.")
my_string = """Multi-
line 
string"""
print(my_string)
"""
It works!
"""

print("\nSometimes an escape character(\\) can be used so the in the code a string can be multi-lined, but the output "
      "does not have a new line there.")
my_string = """Another \
multi- \
line \
string."""
print(my_string)

print("\nElements in a string can be accessed like in a list using brackets([]).")
my_string = "Hello world!"
char = my_string[-1]
print(char)

print("\nIt is possible to copy smaller strings from a larger string using slicing. Standard slicing rules apply.")
substring = my_string[1:5]
print(substring)
substring = my_string[:5]
print(substring)
substring = my_string[5:]
print(substring)
substring = my_string[::-1]
print(substring)
substring = my_string[::2]
print(substring)

print("\nIt is possible to combine string using concatenation with the plus(+) sign.")
greeting = "Hello"
name = "Emilio"
sentence = greeting + " " + name
print(sentence)

print("\nIt is possible to iterate over a string with a for...in... loop.")
for index in my_string:
    print(index)

print("\nIt is possible to see if a certain substring is in a string using if...in...")
if 'e' in my_string:
    print("Yes, there is an e.")
if 'p' in my_string:
    print("Yes, there is a p.")
else:
    print("No, there isn't a p.")
if 'ell' in my_string:
    print("Yes, there is 'ell'." )

print("\nIt is possible to strip excess white space in a string using .strip(). However, due to a string being immutable,"
      " \nit'll need to be reassigned to the same variable rather than just calling the function.")
my_string = "    Hello world    "
print(my_string)
my_string = my_string.strip()
print(my_string)

print("\nIt is possible to make a string all uppercase or all lowercase with .upper() and .lower().")
my_string = "Hello world!"
print(my_string.upper())
print(my_string.lower())

print("\nIt is possible to check whether a string starts with a specific letter or word with .startswith(). It is case-sensitive.")
print(my_string.startswith('h'))
print(my_string.startswith("Hello"))
print(my_string.startswith('World'))

print("\nIt is possible to also check whether a string ends with a certain character or string with .endswith(). It is case-sensitive.")
print(my_string.endswith('!'))
print(my_string.endswith('World!'))
print(my_string.endswith('Hello'))

