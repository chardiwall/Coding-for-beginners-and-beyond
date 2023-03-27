# ------------ Getting Started with python ------------ 

# A variable is like a label that points to a special box in the computer's memory. 
# This box holds a value, like a number or a word. So, when we use a variable in a program, we are really using the value stored in that special box.
# in simple we use variable to store data and access that data.

# We create varible like following
var = 0 # Think of "var" like a box where we can store a number, and the number we put inside the box is 5. So now, whenever we talk about "var", we're really talking about the number 5."


# There are 4 different types data we can store in variable.
# String meaning text (i.e. any sequence of {A-Z, a-z, 0-9, !, @, #, $, %, ^, &, *, (, ), -, +, /, {, },|, \, ", ', ?, ., , and even emojies}
# space is not allowed in the middle of varible name.
name = "Python is fun" # string always sorronded with double qoutes or single qoutes.

# Integer numbers from -infinity to +infinity
num = 99

# Floating or Decimal Numbers (i.e. fractional numbers)
floating_point = 5.5

# Boolean (i.e. True, False)
is_true = True

# Variable naming conventions
# 1. Variable name can only contain small and capital english letters number and underscore(_).
# 2. Variable name can begin with letters or underscore, otherwise it will give error.

# 3. keep Varible names descriptive. so that other can understand the purpose or guess the type of value stored
# e.g. if you want to store the name of the user then do the following:
# first_name and secon_name or full_name rather then fn and sn
# using short variable name is a bad practice and try avoid it

# 4. when combining two name for variable name keep the following convention as a best practice.
# a: snack case: when combining multiple names use underscore after each word but not in the begining and end.
first_name = "Ahmad"

# b: camel case: when combining two names Capitalize the first word of coming words.
firstName = "Ahmad"


# Note: python is case sensitive so first_name and First_Name is not equal. these are two different variables.

# to display information to the screen use use print function.
# a function is a pre-written code for achieving a specific task in this case displying information.
# a function takes input (i.e. additinal data called aguments in programming) process it and gives us output.
# print is the name of the function.
# we put paranthesis "()" to call that specific function to do work.
# the "Hello World" and first_name are inputs to the function.
print("Hello World") # displaying a simple message to the world from machine.
print(first_name) # we mean the value which is "Ahmad" so "Ahmad" will be printed and not first_name because it is a variable.




# # # # z = x+y
# # # print(x, "+", y, ":" ,x+y)
# # # print(x, "-", y, ":",x-y)
# # # print(x, "*", y, ":",x*y)
# # # print(x, "/", y, ":",x/y)
# # # print(x, "//", y, ":",x//y)
# # # print(x, "%", y, ":",x%y)

# # # print(x, "**", y, ":", x**y)

# # fname = input("enter ur first name:- ")
# # lname = input("enter ur first name:- ")
# # print("welcome Mr." + ' ' + fname + lname)

# # print("*"*9)

# # dob = input("enter ur date of brith")
# # dob = int(dob)
# # realage = 2023-dob
# # print("ur are", realage, "years young man")
# # print("_"*9)


# # Requesting first name form user
# first_name = input("Enter your First Name: ")

# # Requesting last name form user
# last_name = input("Enter your Last Name: ")

# # Greeting user
# print("Welcome Mr. ", first_name, last_name)

# print('*' * 50)

# # Requesting Date of Birth form user
# dob = int(input("Enter your Date of Birth: "))

# # displaing user age
# print("You are ", 2023 - dob, "years old")


# print('-' * 50)
