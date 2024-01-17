# Python

Python review for AI course
https://docs.python.org/3.12/index.html

Coursera course: Programming for everybody (Getting startde with Python)

Pierian Data Python course:

Command line: Allows you to run python scripts directly from the files.
cmd

current directory: cd
contents of directory: dir
move into folder: cd <name of folder>
move up: cd ..
(tab autocompletes options)
clear screen: cls

Intalling python with anaconda distribution:
Jupyter notebooks: shift + enter runs cell
comments: #

Running python code: Three main types of envieroments: text editors, IDEs, notebook enviroments. 
log: print('Hello world')
cmd: py

Course notebooks:
Git and github overview:

Python object and data structure basics:
Data types:

Name        |   Type    |   Description
Integers    |   int     |   Whole numbers
Float       |   Float   |   Num with decimal point  
Strings     |   str     |   Characters "x"
Lists       |   list    |   Ordered sequence of objects
Dictionaries|   dict    |   Unordered key:value pairs
Tuples      |   tup     |   Ordered immutable sequence of objects   
Sets        |   set     |   Unordered collection of unique objects
Booleans    |   bool    |   True or False

Numbers: integers and floating point
Arithmetic: 
addition: +
substraction: -
Multiplication: *
Division: /
floor division: //
Modulo (remainder): %
Power: **

Variable assignments: 
rules for variable names:
Names can not start with a number, there can be no spaces, can't use special characters.
Avoid special keywords like "list" or "str"

Python uses dynamic typing: meaning variable types don't have to be explicitly coded, as opposed to C++ where you have to specify that a variable is an INT for example. 

to identify type: type(var)
Declare variable with "="
a = 5;

(delete variable restarts all variable declarations)

Strings: Sequences of characters withing single or double quotes. 
STrings are ordered sequences, which means they can be indexed or sliced. 
Indexing starts at 0, and you can also use reverse indexing. 
Slicing: [start:stop:step] (Stop goes up to but its not included)

print() function is used to print out strings.

Escape sequences:
 \n -> new line.
 \t -> tab.

 length function: len(str)

 String idnexing and slicing: 

Indexing:
 mystring[0] -> returns first character in a string.

Slicing:
 mystring[2:] -> returns rest of string including index two.
 mystring[:3] -> returns everything up to three (three not included).
 mystring[2:3] -> returns a subsection from index 2 to 3.
 mystring[::2] -> returns string with a step size of two.
mystring[::-1] -> reverses the string.

String properties:
Immutability: Strings don't support item assignment. 
String concatennation: my_Var + "string"
Strings can be multiplicated. 

String methods: Using dot notation

my_var.(methods chown using tab)
Eg:
my_var.upper()
my_var.lower()
my_var.split() -> creates a list off of a string based on white space or based on the letter you pass as a parameter. 

Print formatting:
print("string" + str_var)
.format(): Uses {} as placeholders for the variables you're going to use.
'String here {} then also{}'.format('something1','something2')
Works with indexing: 'the {2}{1}{3}'.format('fox','brown','fox')
Works with key:value pairs:
Eg. 
print('The {q}{b}{f}'.format(f='fox',b='brown',q='quick'))

String literals (like JS): use the f before the string.
print(f'Hello, my name is {my_var}')

Lists:
Lists are ordered sequences that can hold a variety of object types. 
They use [] brackets and commas to separate the objects in the list. 
Lists support indexing and slicing, and they can be nested and have useful methods.

Dictionaries:
Unordered mappings for storing objects, using key:value pairs.
{'key1':'value1','key2':'value2'}
Dictionaries: objects retrieved by key name (can't be sorted)
Lists: objects retrieved by location (slice o index)

Curly syntax:
my_dict = {'key1':'value1','key2':'value2'}

print(my_dict['key1'])

Dictionaries can hold lists and other dictionaries as well as other data types. 
Key calls can be stacked: my_dict['key1']['subkey1']

To assign new key value pair: d['new_key] = 'new_value'
Dictionary methods: 
dict.keys()
dict.values()
dict.items()

Tuples:
Similar to lists, but they are immutable. Once an element is assigned, you can't grab it and modify it.
Uses parentheses:

my_tuple = (1,2,3)

Methods:
my_tuple.count(val)
my_tuple.index(val)

Sets:
Unordered collections of unique elements. 

my_set = set()
my_set.add(1)

Booleans:
Operators that convey either True or False statements.
greater than: >

Basic file I/O:

Only in Jupyter:
 %%writefile my_file.txt
Content

my_file.read()
my_file.seek(0)
my_file.readlines()
my_file.close()

File locations:

My_file = open("C:\\Users\\test.txt")

with open("my_file.txt",mode='r') as my_file:
    contents = my_file.read()

Comparison operators:
Equality: ==
Not equal: !=
Greater than: >
Smaller than: <
Greater or equal: >=
Smaller or equal: <=

Logical operator keywords:
and: 1 < 2 and 2 < 3
or: 1 < 2 or 2 < 3
not: returns oppositve booleand of the comparison: not(1 == 1)

Statements: control flow 
if, elif, else:
Python uses an indentation system, the control flow uses colons and indentation (whitespace). 

if some_condition:
    #Execute some code
elif other_condition:
    #Other code
else:
    #Some other code

For loops:
Iterable objects can be operated upon by for loops. Perform an action for every item in an object like a list.

for item_name in my_iterable:
    print(item_name)

for num in mylist:
    if num % 2 == 0:
        print('even')
    else:
        print('odd number')

Tuple unpacking: 
Use the iterable variable in the for loop as a tuple, gives acces to the individual items:

my_list = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in my_list:
    print(b)

Iterate through dictionaries:

d = {'k1':'one','k2':'two'}

for key,value in d.items():
    print(key)