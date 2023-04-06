"""This is a simple program that read data about the user."""

name = input( 'please enter your name: '.capitalize() )

gender = input('please specify you gander(m/f): '.capitalize())

if gender[0] == 'm' or gender[0] == 'M':
    print('Greetings Mr. ', name)

else:
    is_married = input( 'are you married(Y/N)!: '.capitalize() )
    if is_married[0].upper() == 'Y':
      print('Greetings Miss. ', name)
    else:
      print(f"Greetings Mirs.{name}")
  

temp = input('Enter Tempreture(20c/20f): ')

letter = temp[-1]
num = int(temp[0:-1])


if letter.lower() == 'c':
  fahrenheit = num * 9/5 + 32
  print(f'{num} Celsius is equal to {fahrenheit} Fahrenheit')

else:
  celsius  = (num - 32) * 9/5
  print(f'{num} Fahrenheit is equal to {celsius} Celsius')

print(celsius)
print(fahrenheit)