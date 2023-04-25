# --------------------- conditions ---------------------------
# Conditions in Python allow us to make decisions based on whether a certain condition is true or false.
# We can use conditions to control the flow of our program and execute different blocks of code depending on the values of certain variables or inputs.
# To make condition in python we need to compare numbers or string.
# To do this we will understand comparison operator first.

# Comparison operators
# To create conditions, we can use comparison operators to compare the values of variables or expressions.

# These are all comparision operators
# 1. == (equals): Checks if two values are equal to each other.
# 2. != (not equals): Checks if two values are not equal to each other.
# 3. < (less than): Checks if the value on the left is less than the value on the right.
# 4. > (greater than): Checks if the value on the left is greater than the value on the right.
# 5. <= (less than or equal to): Checks if the value on the left is less than or equal to the value on the right.
# 6. >= (greater than or equal to): Checks if the value on the left is greater than or equal to the value on the right.

x = 5
y = 10

print(f"{x} == {y}: ", x == y)  # False
print(f"{x} != {y}: ", x != y)  # True
print(f"{x} < {y}: ", x < y)  # True
print(f"{x} > {y}: ", x > y)  # False
print(f"{x} <= {y}: ", x <= y)  # True
print(f"{x} >= {y}: ", x >= y)  # False

# if Statement
# The most common way to use conditions in Python is with if statements.
# An if statement allows us to execute a block of code only if a certain condition is true.

# Here's the basic syntax of an if statement:
# if condition:  # note ':' this means that the following lines only will be executed if the conditions is true.
# code to execute if condition is true # note indentation it means the this line is part of the if statement.


# Example:
if x < y:
    print(
        "x is less than y"
    )  # in this the condition is true and it will output this msg
# checks if x is less then y.
# if x is less then y that will mean that the condition is true and 25 line will execute.
# if x is greater then y then the condtioin will be false and 25 line will not execute.

# Example:
x = 5
y = 10

if x < y:
    print("x is less than y")
else:
    print("x is greater than or equal to y")

# In this example, we use an if statement to check if x is less than y.
# If the condition is true, we print a message saying that x is less than y.
# If the condition is false, we use the else keyword to execute a different block of code that prints a message saying that x is greater than or equal to y.

# in general
# The if statement in Python is used for conditional execution of code. In the code above, x is compared to y using the less than operator <.
# If the condition is True, then the code inside the if block is executed. In this case, the code inside the if block is to print the message "x is less than y".
# If the condition is False, then the code inside the if block is not executed.


# elif Statements
# We can also use elif statements to add more conditions to our if statements.
# An elif statement allows us to check an additional condition if the previous conditions were false.

# Structure
# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if all conditions are false

# Example:
x = 5
y = 10

if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")
# In this example, we use an if statement to check if x is less than y.
# If the condition is true, we print a message saying that x is less than y.
# If the condition is false, we use an elif statement to check if x is equal to y.
# If this condition is true, we print a message saying that x is equal to y.
# If both conditions are false, we use the else keyword to execute a different block of code that prints a message saying that x is greater than y.


# Nested if Statements
# We can also nest if statements inside other if statements to create more complex conditions.
# Here's an example of how we can use nested if statements to create a condition:
x = 5
y = 10

if x < y:
    if x > 0:
        print("x is less than y and greater than 0")
    else:
        print("x is less than y but not greater than 0")
else:
    print("x is greater than or equal to y")

# In this example, we use an if statement to check if x is less than y.
# If the condition is true, we use another if statement to check if x is greater than 0.
# If this condition is true, we print a message saying that x is less than y and greater than 0.
# If this condition is false, we print a different message saying that x is less than y but not greater than 0.
# If the first condition is false, we use the else keyword to execute a different block of code that prints a message saying that x is greater than or equal to y.


# Logical Operators
# We can also use logical operators to combine multiple conditions and create more complex conditions.
# Here are the logical operators in Python:

# 1. and: Checks if both conditions are true.
# 2. or: Checks if either condition is true (at least one).
# 3. not: Negates the condition, returning the opposite boolean value.
# 4. in: Tests if a given value is present in a sequence or collection.
# 5. is: Checks if two objects are the same object in memory. In other words, it checks if two variables point to the same memory location.
# Here's an example of how we can use logical operators to create a condition:
x = 5
y = 10

if x < y and x > 0:
    print("x is less than y and greater than 0")
elif x < y or y < 0:
    print("either x is less than y or y is less than 0")
else:
    print("x is greater than or equal to y")
# In this example, we use the 'and' operator to check if x is less than y and greater than 0.
# If this condition is true, we print a message saying that x is less than y and greater than 0.
# If the first condition is false, we use the or operator to check if either x is less than y or y is less than 0.
# If this condition is true, we print a different message saying that either x is less than y or y is less than 0.
# If both conditions are false, we use the else keyword to execute a different block of code that prints a message saying that x is greater than or equal to y.


# Using "in" with a string
string = "Hello, world!"
print("H" in string)  # True
print("hello" in string)  # False

# using is wth a string
a = "ahmad"
b = a

if a is b:
    print("a and b point to the same memory location")
else:
    print("a and b do not point to the same memory location")


# Bitwise operators
# Bitwise operators are used to perform operations on binary numbers.
# A binary number is a number expressed in the base-2 numeral system, which uses only two digits: 0 and 1.
# In contrast, the decimal (base-10) system we use in everyday life uses 10 digits (0-9).

# There are several bitwise operators in Python:

# 1. Bitwise AND (&): returns 1 if both bits are 1
# 2. Bitwise OR (|): returns 1 if either bit is 1
# 3. Bitwise XOR (^): returns 1 if the bits are different (one is 1 and the other is 0)
# 4. Bitwise NOT (~): inverts all the bits (0 becomes 1 and 1 becomes 0)
# 5. Left shift (<<): shifts the bits to the left by a specified number of places
# 6. Right shift (>>): shifts the bits to the right by a specified number of places
# 7. Here's an example of using the bitwise AND operator:

a = 60  # binary: 0011 1100
b = 13  # binary: 0000 1101

c = a & b  # binary: 0000 1100
# In this example, we have two variables a and b that are represented in binary form as 0011 1100 and 0000 1101, respectively.
# We then use the bitwise AND operator (&) to combine these two numbers, which results in 0000 1100.
# This is because the operator compares each bit position in a and b, and only returns a 1 if both bits are 1.


# Similarly, here's an example of using the bitwise OR operator:

a = 60  # binary: 0011 1100
b = 13  # binary: 0000 1101

c = a | b  # binary: 0011 1101
# In this example, we use the bitwise OR operator (|) to combine a and b.
# The operator compares each bit position in a and b, and returns a 1 if either bit is 1.
# This results in the binary number 0011 1101, which is equivalent to the decimal number 61.


# Using the bitwise XOR operator (^):
a = 60  # binary: 0011 1100
b = 13  # binary: 0000 1101

c = a ^ b  # binary: 0011 0001
# In this example, we use the bitwise XOR operator (^) to combine a and b.
# The operator compares each bit position in a and b, and returns a 1 if the bits are different (one is 1 and the other is 0).
# This results in the binary number 0011 0001, which is equivalent to the decimal number 49.


# Using the bitwise NOT operator (~):
a = 60  # binary: 0011 1100

c = ~a  # binary: 1100 0011
# In this example, we use the bitwise NOT operator (~) to invert all the bits in a.
# This results in the binary number 1100 0011, which is equivalent to the decimal number -61 (due to the way two's complement representation works).


# Using the left shift operator (<<):
a = 60  # binary: 0011 1100

c = a << 2  # binary: 1111 0000
# In this example, we use the left shift operator (<<) to shift the bits in a to the left by 2 places.
# This results in the binary number 1111 0000, which is equivalent to the decimal number 240.

# Using the right shift operator (>>):
a = 60  # binary: 0011 1100

c = a >> 2  # binary: 0000 1111
# In this example, we use the right shift operator (>>) to shift the bits in a to the right by 2 places.
# This results in the binary number 0000 1111, which is equivalent to the decimal number 15.
