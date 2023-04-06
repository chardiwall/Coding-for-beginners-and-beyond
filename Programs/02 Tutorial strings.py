#    -------------------------- Strings (text) -------------------------

# A string is a bunch of letters or symbols or bouth that we put inside quotation marks.
# In Python, strings are a type of data that can be used to store and manipulate text.
# following are examples of string:
sample_string_01 = "This is a simple string enclosed in double qoutes"
sample_string_01 = 'This is a simple string enclosed in single qoutes'

# In Python, there are two types of strings:
# Single-line strings:
# Single-line strings are the most common type of strings in Python. 
# They are created by enclosing a sequence of characters in single quotes ('...') or double quotes ("...").
# with enter it breaks. e.g. sample_string_01 and sample_string_02.

# Sometimes we need to write a long sentence or message that can't fit on one line.
# To do this in Python, we can use something called a "backslash" at the end of each line to join the different lines together.
# For example, if we wanted to print the sentence "I love playing video games on my computer", but it was too long to fit on one line, we could split it up like this:

print("I love playing video games on \
my computer")

# The backslash tells Python that the sentence continues on the next line, so when we run the code, it will print the whole sentence on one line.
# It's important to remember that when we use a backslash to join lines in a single-line string, there will be no "enter" or line break in the printed text.

# 2. Multi-line strings:
# Multi-line strings are used when a string needs to span across multiple lines.
# They are created by enclosing a sequence of characters in triple quotes ("""...""") or ('''...'''). Here's an example:


sample_string_04 = """this is a sample 
of multiple line 
comment, 
that actually prints
in deffernet lines.
"""

sample_string_05 = '''this is a sample 
of multiple line 
comment, 
that actually prints
in deffernet lines.
'''

# Note: Qoutes that surrounds string called delimiters because it tell python where string strats and where it ends.

# Note: there is no difference using double qoutation (") or single  qoutation (').
# it is more like a personal preference


# Arithmatic Operation on String.
# there are two operations related to string:

# 1. String Cancatination (+).
# here we join or combine strings to make a new string. here is an example:
first_name = "Ahmad"
second_name = "Mustafa"
full_name = first_name+" "+second_name # this called string concatincation
print("full_name: ", full_name) # prints: Ahmad Mustafa

#2. String replication.
name = "ahmad"
replicated_name = name * 5 #this will create 5 copy of the string "ahmad" such like: "ahmadahmadahmadahmadahmad".
print("replicated_name: ", replicated_name)

# String indexing and slicing
# Each character in string has number position called an index.
# In python indexing and slicing can be achieved using supscription operator "[]".
# We can access Nth positioned character by putting the number N between square brackets [N] immediatly after string without space.
name = "Ahmad Mustafa"
print("name[0]:", name[0]) # prints A    

# Note in python and many other programming languages counting starts from 0 and not 1.

print("name[6]: ", name[6]) # displays the word M

# in python we have two type of indexing
# 1. postive indexing which is 0->A, 1->h, 2->m, 3->a and so on...
# 2. negative indexing which -1->a, -2->f, -3->a, -4->t and so on...
# negative indexing is backward traversing
print("name[-5]: ", name[-5]) # prints s

# We can access multiple character at once called slicing like following.
print("name[1:4]: ", name[1:4]) # this means from 1th postion upto 4th but 4th charecter is not included  hma.
print("name[3:8]: ", name[3:8]) # prints "ad mu:

print("name[-6: -1]: ", name[-6: -1]) # prints "ustaf"
print("name[1: -3]: ", name[1: -3]) # prints "hmad Must"
print("name[-1: -3]: ", name[-1: -3]) # prints "" because -1 means last word the.

print("name[3:]: ", name[3:]) # prints "ad Mustafa" from third postion upto end.
print("name[:7]: ", name[:7]) # prints "Ahmad M" from first position upto 7th postion.

print("name[:]: ", name[:]) # prints "Ahmad Mustafa" from begining upto end

# strin[start: end: steps]
print("name[::2]: ", name[::2]) # amdMsaa   # this meanse every second word is printed.
print("name[::3]: ", name[::3]) # AaMta  # every third word is prented hence step is 3.
print("name[::-1]: ", name[::-1]) # afatsuM damaH  # every third word is prented hence step is 3.



# String operations using function
# There are two types of function
# 1. general function that works with any data type: str, int or float.

# 2. A special kind of function called method which is specific to data type.
# method is accessed using "." after variable name so we have variable.method().

name = "Ahmad Mustafa" # name is variable of string datatype

# general function
# 1. Specifies the length of string
len_of_name = len(name) # We use len function that returns 


# string methods
print( "name.upper(): ", name.upper() ) # Converts the value of name to upper-case. # AHMAD MUSTAFA
print( "name.lower(): ", name.lower() ) # Converts the value of name to lower-case. # ahmad mustafa
print( "name.count('a'): ", name.count("a") ) # Counts the repetition of lower 'a' in name. # 3 
print( "name.find('a'): ", name.find('a') ) # Finds the first letter or substring and return the index. # 3
print( "name.replace('a', '4'): ", name.replace('a', '4') ) # Replaces all occurance of lower 'a' with letter '4'. # Ahm4d Must4f4
print( "name.strip(): ", name.strip() )  # Remove white space from the begining and from the end of the string.
print( "name.isdigit(): ", name.isdigit() ) # Returns true if name variable only contanins numbers. # False
print( "name.startswith('A'): ", name.startswith('A') ) # Returns true if the string in name variable starts with A. # True



# Note: Strings are Immutable.
# Means that once we assign a string to a variable it cannot be changed.

# So how the replace function changes the text?
# well it does not changes the actual name.
# The replace function copy the value of name and make changes to it.
# Then it returns the altered or changed text. which is then printed to the screen and can be stored any where.
# so if we print the actual value it will not be changed.
print("Test:", name.replace('Ahmad', 'Mahmood')) # prints Mahmood Mustafa
print("Test: ", name) # prints Ahmad Mustafa
# The key take away is that the name variable itself is not changed.

# Immutable meanse we cannot do following:
# for example you want to change the letter 'u' in 'Ahmad Mustafa' to o. you might do this:
# name[8]='o' so this cannot happen and will give error.
# instead we do ether:
# name.replace('u', 'o')  or
# name.replace('Mustafa', 'Mostafa')
