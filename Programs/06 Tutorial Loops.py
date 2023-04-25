# Loops in Python are a way to repeatedly execute a block of code. 
# They are used when you want to perform a specific operation a certain number of times or until a certain condition is met. 
# There are two types of loops in Python: for loops and while loops.

# For loops are used when you know the exact number of times you want to execute a block of code. 
# They iterate over a sequence of values and execute the block of code for each value. The syntax for a for loop is as follows:

for variable in "sequence":
    'block of code'

# In the above syntax, variable is a new variable that is created each time the loop is executed and is set to the current value in the sequence. 
# The block of code is indented and is executed once for each value in the sequence.

# Here is an example of a for loop that prints the numbers 1 through 5:

for i in range(1, 6):
    print(i)

# The range() function generates a sequence of numbers from the starting value (inclusive) to the ending value (exclusive). In this case, the sequence is 1, 2, 3, 4, 5.

# While loops, on the other hand, are used when you want to repeatedly execute a block of code until a certain condition is met. The syntax for a while loop is as follows:

while 'condition':
    'block of code'

# In the above syntax, condition is a Boolean expression that is evaluated before each iteration of the loop. 
# The block of code is executed repeatedly as long as the condition is True. Once the condition is False, the loop exits.

# Here is an example of a while loop that prints the numbers 1 through 5:

i = 1
while i <= 5:
    print(i)
    i += 1

# In this example, the condition is i <= 5. The block of code is executed repeatedly as long as i is less than or equal to 5.
# i is incremented by 1 each time the block of code is executed, so eventually the condition will become False and the loop will exit.



# Write a program that prints out the numbers 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)

# Write a program that prints out the even numbers between 1 and 20 using a while loop.
i = 2
while i <= 20:
    print(i)
    i += 2

# Write a program that asks the user to enter a number, then prints out the sum of all the numbers from 1 to that number.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of numbers from 1 to", n, "is", sum)

# Write a program that prints out the prime numbers between 1 and 20.
for num in range(2, 20):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)








