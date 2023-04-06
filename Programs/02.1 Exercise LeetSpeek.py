# Leetspeak program --- informal language consist of letters and numbers.
print(' LeetSpeak Converstion Program'.center(80, fill='*'))

# Steps
# 1. Read user name and store it in variable name.
# Note: to read information from user we use input('message') function. where the input or argument message tells the user what are asking for.
name = input( 'please enter your name: '.capitalize() ) # capitalize is a string methode that converts the begning of every word capitalize.

# 2. replace the following:
# a → 4
# b → 8
# e → 3
# l → 1
# S → 5
# t → 7

name = name.replace('a', str(4))
name = name.replace('b', str(8))
name = name.replace('e', str(3))
name = name.replace('l', str(1))
name = name.replace('s', str(5))
name = name.replace('t', str(7))


# display the altered text
print("final Text: ", name)