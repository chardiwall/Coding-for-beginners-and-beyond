# Converting Temperature program with the help of functions

# Task #01
# Read user name .
# Read the gender of the user.
# If the person is greet them with the word Mr.
# else if the person is female ask them whether they are married or not.
# If they are married greet them with the word Mrs.
# Else grade them with the word Ms.

# Task 02
# Read the temperature in the following format 20f or 20c
# If the last character of the entered string is C then convert Celsius to Fahrenheit using the following formula
# Fahrenheit = celsius * 9/5 + 32
# Else calculate Celsius using:
# celsius = (Fahrenheit - 32) * 5/9


def greet_user():
    name = input("Please enter your name: ").capitalize()
    gender = input("Please specify your gender (m/f): ").capitalize()
    if gender[0] == "M":
        print(f"Greetings Mr. {name}")
    else:
        is_married = input("Are you married (Y/N)? ").capitalize()
        if is_married[0] == "Y":
            print(f"Greetings Mrs. {name}")
        else:
            print(f"Greetings Ms. {name}")


def convert_temperature():
    temp = input("Enter temperature (e.g. 20C or 20F): ")
    letter = temp[-1]
    num = int(temp[:-1])
    if letter.lower() == "c":
        fahrenheit = num * 9 / 5 + 32
        print(f"{num} Celsius is equal to {fahrenheit} Fahrenheit")
        return num, fahrenheit
    else:
        celsius = (num - 32) * 5 / 9
        print(f"{num} Fahrenheit is equal to {celsius} Celsius")
        return celsius, num


greet_user()
temperature_values = convert_temperature()
print(temperature_values)
