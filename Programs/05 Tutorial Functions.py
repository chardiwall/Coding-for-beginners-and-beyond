# ------------------------- Functions -------------------------------

# Functions are an essential part of programming in Python, as they allow you to group together a set of instructions that can be called and executed multiple times within a program. 
# Essentially, a function is a block of code that performs a specific task.
# Functions in Python have the following basic syntax:

def function_name(parameters):
    # function body
    return 'value'

# The *def* keyword is used to define a function
# *function_name* is the name of the function
# *parameters* are inputs to the function, which can be used within the function
# The *return* statement is used to return a value from the function

# Here's an example of a simple function that adds two numbers:
def add_numbers(a, b):
    return a + b

# To use this function, you would call it and pass in two numbers as arguments:
result = add_numbers(2, 3)
print(result)  # Output: 5

# This function takes two arguments, a and b, and returns their sum.

# Functions can be used to simplify and organize your code, and they can also make it easier to debug errors. 
# By dividing your code into smaller, reusable chunks, you can more easily test and debug each part of your program.
# Here's another example of a function that calculates the area of a circle:
def calculate_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

# In this example, the function calculates the area of a circle based on its radius. 
# The function body contains two variables, pi and area, which are used to calculate the area of the circle.

# Functions can be very powerful and versatile, and they can be used in a wide variety of applications. 
# Some other common uses for functions in Python include:

# Data analysis and manipulation
# Web scraping and automation
# Machine learning and artificial intelligence
# Game development
# And much more!


# in general in every programming language we two kind of functions:
# 1. User Defined functions: These function are discussed earlier.
# it is defined using *def* key word following by the funcion name and paranthesis.
# Syntax:
def function_name(parameters):
    # function body
    return 'value'


# Pre-defined functions

# Pre-defined functions in Python are built-in functions that come with the language and are readily available to use.
# They are a set of functions that perform specific operations without needing to define them first. 
# These functions are designed to simplify programming and reduce the amount of code required to perform common tasks.

# Here are a few examples of pre-defined functions in Python:

# print(): This function is used to print a message or value to the console. 
# It takes a string or value as an argument and displays it on the screen. For example:
print("Hello, World!")   # Output: Hello, World!

# len(): This function is used to get the length of an object like a string, list, tuple, or dictionary. It returns the number of items or characters in the object. For example:
string = "Hello, World!"
length = len(string)
print(length)   # Output: 13

# type(): This function is used to get the data type of an object. It returns the class or type of the object. For example:
number = 5
print(type(number))   # Output: <class 'int'>

# input(): This function is used to get user input from the console. It displays a prompt to the user and waits for them to enter a value. For example:
name = input("What is your name? ")
print("Hello, " + name + "!")


# Note: These are just a few examples of the many pre-defined functions in Python. They are already available to use and do not require any additional coding to implement. By using these functions, you can simplify your code and perform common tasks more efficiently.