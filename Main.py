#Strings: ordered, immutable, text representation
from timeit import default_timer as timer

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

print("\nIt is possible to get the index of the first iteration of something in a string. It will return a -1 if it doesn't find "
      "anything.")
print(my_string.find("o"))
print(my_string.find('ello'))
print(my_string.find('p'))

print("\nIt is possible to count how many times a certain character appears in a string using .count().")
print(my_string.count('l'))

print("\nYou can use .replace() to generate a new string replacing certain characters with new ones. It is case-sensitive.")
new_string = my_string.replace('world', 'Universe')
print(new_string)

print("\nIt is possible to generate a list using a string and have every element be an individual word using .split(). "
      "\nThe default delimiter is a space, so it might be necessary to specify a specific delimiter depending on the case.")
my_string = "How are you doing?"
my_list = my_string.split()
print(my_list)
comma_string = "How,are,you,doing?"
my_list = comma_string.split()
print(my_list)
my_list = comma_string.split(',')
print(my_list)

print("\nIt is possible to convert a list into a string using "".(). Whatever is put in the quotes will be what's put in"
      " between every element in the list.")
new_string = ''.join(my_list)
print(new_string)
new_string = ' '.join(my_list)
print(new_string)

print("\nSome might use a for loop to add elements of a list into a string, but that will take much longer time than "
      "using the .join function.")
my_list = ['a'] * 1000000
#Bad Python code
start = timer()
for index in my_list:
    my_string += index
stop = timer()
print(stop - start)
#Good Python code
start = timer()
my_string = "".join(my_list)
stop = timer()
print(stop - start)

#There are a few ways to format a string. %, .format(), f-Strings
print("\nThere are a few different ways to format a string using either the percent(%) sign, using the .format() function, "
      "or using f-Strings.")
print("\nFor percent sign usage, the proper symbol after the percent sign must match the type of variable being placed. "
      "s for strings, d for decimals/integers, and f for float numbers. \nIt is possible to modify further by adding a "
      "decimal in between the percent sign and symbol to indicate how many spaces to print.")
var = "Tom"
percent_string = "The variable is %s" % var
print(percent_string)

var = 3
percent_string = "The variable is %d" % var
print(percent_string)

var = 3.123456789
percent_string = "The variable is %f" % var
print(percent_string)

percent_string = "The variable is %.2f" % var
print(percent_string)

print("\nUsing the .format() function involves placing curly brackets({}) in the string where the variable will be and then putting"
      " which variables in the parentheses of the function. \nMultiple variables can be placed at once, as well as,"
      " be modified by placing modifiers in the curly brackets.")
format_string = "The variable is {}".format(var)
print(format_string)

format_string = "The variable is {:.2f}".format(var)
print(format_string)

var2 = 6
format_string = "The variable is {:.3f} and {}".format(var, var2)
print(format_string)

print("\nF-Strings involve putting f before the quotes("") and putting curly brackets({}) with the desired variables inside. "
      "where it is desired. \nIt is also possible to modify the results within the curly brackets.")
f_string = f"The variables are {var*2} and {var2}"
print(f_string)