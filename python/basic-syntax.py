# This here is a comment
# Comments are plain text, it doesn't run, it's purpose is to document a code base
"""
There are multiline comments
and this is how you write them
they're pretty quirky in python compared to others
"""

#As you can see there's no 'boilerplate' code, you simply begin writing python
#Lines straight away

x = 5 # python is dynamically typed, you don't need to explicitly write the type of a variable
x: int = 5 #this is correct, and preferred sometimes, as it helps with readability when the code base becomes more complex

#python has many variable types such as:
integer: int
decimalNumbers: float
stringsOfCharacters: str
booleanValues: bool
theNoneType: None 

#python's output function
print(x) # the output should be 5

#if we use the type function in conjuction with the print function
#we can know the type of a variable
print(type(x)) # should show us that x is an int

#python can intake user input with the following function
input("Enter Something: ") #when run, the user will be propmted to enter a value

#to make use of these inputs, we can store it in a variable
name = input("Enter your name: ") 
print(name)

#when run, the user will be propmted to enter a name, then it will be output the name they entered

print(type(name)) #will output 'str', as in strings, all inputs you give the input() function are automatically converted to strings, even if you enter only numbers

#to convert the data type of a value, you can use one of these functions
int()
float()
str()
bool()

#so now, we can do some basic arithmetic
#the operations symbols are: + - / *

a = 12
b = int(input("Enter a number: "))
# if you enter a string, it'll throw up an error, we'll see how to handle that later
print(a + b)

# and that's it for the basics :D
