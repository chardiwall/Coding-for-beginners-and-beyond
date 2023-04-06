# importing math module to extend the default functionality of python.
# see line 192 for further clarification.
import math

#     ------------------------ Numbers ----------------------
# we have 3 types of number in python
# 1. integer -> -infinity upto +infinity. cannot have point or fractional number. e.g. 0
# 2. floating  number or decimal number -> -infinity, +infinity. comes in point number shape. e.g. 0.0.
# 3. complex number -> a+bj

#example of integer
integer = 5

# to type is python built-in function that takes object as input and tell us what is the data type of that object.
# in print function we can give multiple inputs which is sperated with ','.
print("type: ", type(integer), "value", integer)

#example of floating point
floating_number = 5.5
print("type: ", type(floating_number), "value", floating_number)

# complex number
complex_number = 5+6j
print("type: ", type(complex_number), "value", complex_number)



# operations on integer numbers:

# Note: we have two kind of operators:
# 1. Unary Operators: as the name indicates here we have only one operator and one operand. almost always the operator comes to the left of operands.
# +5 or -5 here (+) is an operator indicates positive number and (5) is the operand being indicated. same goes for (-).
print(-5) # prints -5
print(5) # prints 5

# 2. Binary Operators: here we have two operands and one operator in the middle of operator.
# 4+3 --- 4 and 3 are operands and + is an operator used to add two numbers.

x = 4
y = 3

# We use + to add two numbers.
print(x, "+",  y, "= " , x+y) #x+y= 7

# We use - to fined differnce between two numbers.
print(x, "-",  y, "= ", x-y)  #x-y= 1

# We use * to multiply two numbers.
print(x, "*",  y, "= ", x*y)  #x*y= 12

# We use / to divide two numbers. here x is the nominator and y is the denominator.
print(x, "/",  y, "= ", x/y)  #x/y= 1.3333333333

# // this symble is called floor division wich gives us integer number as a result and not fractional number.
print(x, "//", y, "= ", x//y) #x//y= 1

# % this symbole is called mod or modulus or reminder, which finds the reminder of two number in division.
print(x, "%",  y, "= ", x%y)  #x%y= 1

# in python ** is used for finding exponential values. here x is the base and y  is the power.
print(x, "**", y, "= ", x**y) #x**y= 64



# operations on floating numbers:

x = 4.5
y = 3.3

# We use + to add two numbers.
print(x, "+",  y, "= " , x+y) #x+y= 7.8

# We use - to fined differnce between two numbers.
print(x, "-",  y, "= ", x-y)  #x-y= 1.2000000000000002

# We use * to multiply two numbers.
print(x, "*",  y, "= ", x*y)  #x*y= 14.85

# We use / to divide two numbers. here x is the nominator and y is the denominator.
print(x, "/",  y, "= ", x/y)  #x/y= 1.3636363636363638

# even if this works with floating number but the floor division is not for floating numbers. it is only for integer numbers.
print(x, "//", y, "= ", x//y) #x//y= 1.0

# same for reminder it is not okay to use reminder(%) with decimal numbers.
print(x, "%",  y, "= ", x%y)  #x%y= 1.2000000000000002

# in python ** is used for finding exponential values. here x is the base and y  is the power.
print(x, "**", y, "= ", x**y) #x**y= 143.08736809014272


# operations on complex numbers:

x = 6+ 7j
y = 3+ 2j

# We use + to add two numbers.
print(x, "+",  y, "= " , x+y) #x+y= (9+9j)

# We use - to fined differnce between two numbers.
print(x, "-",  y, "= ", x-y)  #x-y= (3+5j)

# We use * to multiply two numbers.
print(x, "*",  y, "= ", x*y)  #x*y= (4+33j)

# We use / to divide two numbers. here x is the nominator and y is the denominator.
print(x, "/",  y, "= ", x/y)  #x/y= (2.4615384615384617+0.6923076923076924j)

# in python ** is used for finding exponential values. here x is the base and y  is the power.
print(x, "**", y, "= ", x**y) #x**y= (102.61359530069451+94.82608377973663j)


# Note: for complex number we do not have floor division (//) and reminder (%) operators.

# Type Casting (data-type conversion):
# In general, in programming we have two kind of Type casting.
# 1. explicit, 2. implicit

# Explicit type casting is done by use. We have to tell the machine that we are doing a specific type converion.
# In python we have following type castings:
# from string to int → int("5")
# from string to int → float("5.5")
# for the above two conversion there is only one rule and that is that string should not have any alphabitic letter.
# e.g. int("5k") will give error because it has a letter. same goes for float.
# from string to complex number → complex("5+4j")

# from int to str → str(5)
# from int to float → float(5.5)
# from int to complex → complex(4)

# from float to str → str(5.5)
# from float to int → int(5.5)
# from float to complex → complex(4.3)



# we use string literals to read numbers easily
# in every day life 10,000,000 -> in python 10_000_000
# we cannot use comma for the same purpuse as we use in real life
# 10,000,000 will mean 3 different number and not one
long_num = 10_000_000
print(long_num)

# complex operations
exp = 2+(3*(4-3))+6*7/8**9
print(f"2+(3*(4-3))+6*7/8**9 = ", exp)


# dealing with functions in numbers
# General function -> works with almost any data-type
# abs() finding absolout value.
abs_value = abs(-5)
print("The absolute value of -5: ", abs_value) #5

# round - Round a number to a given precision in decimal digits.
num= 5.378
print(f"round of {num}: ", round(num, 1))

# pow(base, exponent),  calculates the power of a number
print(f"pow of {num}, {2}: ", pow(num, 2))

# pow(base, exponent, reminder) -> calculates (base**exponent) % reminder
num = int(num)
print(f"pow of {num}, {2}: ", pow(num, 2, 2))

# divmode -> returns the division and the reminder of two numbers at once.
print(f"division and reminder of 15, 4:", divmod(15,4))


# ----------------- External functions -------------

# Note to work with external files or modules we have to make it part of or python file. we do that as follow:
# import math -> in this case math is an external file that contains python code.
# this file came with python installation. so when we install python environment these modules shiped with it.
# now we can use 'math' module to calculate complex operations like sin or asin or sinh or square root.

# Note: we have to use this line 'import math' at the begining of file. means in the first line


x = 90
y = 10

# Return the cosine of x.
print( f"cosine of {x} = ", math.cos(x) )

# Return the sin of x.
print( f"sine of {x} = ", math.sin(x) )

# Return the cube root of x.
print( f"cube root of {x} = ", math.cbrt(x) )

# Return the square root of x.
print( f"square root of {x} = ", math.sqrt(x) )

# Return the factorial of y.
print( f"factorial of {x} = ", math.factorial(y) )

# truncates decimal part from a number.
print( f"floor of {x+0.5} = ", math.floor(x+0.5) )

# increment a number with one and removes decimal part of the number.
print( f"ceil of {x+0.5} = ", math.ceil(x+0.5) )


# Note: there are a lot of other functionalities in math module you can check it using folloing lin of code.
help(math)