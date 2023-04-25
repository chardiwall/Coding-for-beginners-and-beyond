# ------------------------ FizzBuzz --------------------------
# This code prompts the user to input a number and then checks whether the input is a valid integer.
# If the input is valid, it checks if the number is divisible by 3 and 5, in which case it prints "FizzBuzz".
# If the number is only divisible by 3, it prints "fizz".
# If the number is only divisible by 5, it prints "Buzz".
# If the number is not divisible by either 3 or 5, it prints an error message.


# The first line of the code prompts the user to input a number and stores it in the variable "num".
num = input("Please Enter a Number: ")
# The input value is initially a string, so the next line checks whether it consists entirely of digits using the "isdigit()" method. If it does, it converts the string to an integer using the "int()" function.
if num.isdigit():
    num = int(num)

    # The code then checks if the integer is divisible by both 3 and 5 using the modulo operator (%). If it is, it prints "FizzBuzz".
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")

    # If the integer is not divisible by both 3 and 5, the code checks if it is only divisible by 3 using the modulo operator. If it is, it prints "fizz".
    elif num % 3 == 0:
        print("fizz")

    # If the integer is not divisible by both 3 and 5 and is not only divisible by 3, the code checks if it is only divisible by 5 using the modulo operator. If it is, it prints "Buzz".
    elif num % 5 == 0:
        print("Buzz")

    # If the integer is not divisible by either 3 or 5, it prints an error message.
    else:
        print("Error: Wrong Number!!!")

    # If the input value is not a valid integer, the code prints an error message.
else:
    print("Error: Wrong Input, Please Enter a Number!!!")
