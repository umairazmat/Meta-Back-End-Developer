print("Hello World 👋")

# Output: Hello World 👋

# Python Syntax
# Python is a case sensitive language.
# Python uses indentation to define a block of code.
# Python uses # to start writing a comment.

# Addition
y = 1 +         3
print(y)        # Output: 4

x = 1 +         3\
+5
print(x)        # Output: 9

name= "UMAIR"
if name == "UMAIR":
    print("Hello UMAIR")    # Output: Hello UMAIR

# Python Variables and Functions
def add(x, y):
    return x + y
add(1, 2)       # Output: 3

#assigning values to variables

a , b , c = 1 , 2 , 3
print(a,b,c)        # Output: 1

# Python Data Types
# Python has five standard data types −
# Numbers
# String
# List
# Tuple
# Dictionary

# Python Numbers
# Python supports four different numerical types −
# int (signed integers)
# long (long integers, they can also be represented in octal and hexadecimal)
# float (floating point real values)
# complex (complex numbers)

num = 56;
print(type(num))     # Output: <class 'int'>

student = "UMAIR";
print(type(student))     # Output: <class 'str'>
print(student[0])       # Output: U
print(student[2])       # Output: A
print(student[4])       # Output: R
print(student[-1])      # Output: R
print(len(student))    # Output: 5 

score = 3.5;
print(type(score))     # Output: <class 'float'>

list = [1,2,3,4,5];
print(type(list))     # Output: <class 'list'>

tuple = (1,2,3,4,5);
print(type(tuple))     # Output: <class 'tuple'>

dict = {1:"one", 2:"two", 3:"three"};
print(type(dict))     # Output: <class 'dict'>

#input function
name = input("Enter your name: ")
print("Hello " + name)
