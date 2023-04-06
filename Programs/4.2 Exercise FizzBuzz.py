num = input('Please Enter a Number: ')# 25
if num.isdigit():
  num = int(num)

  if num % 5 == 0 and num % 3 ==0:
    print("FizzBuzz")
  
  elif num % 3 == 0:
    print('fizz')

  elif num % 5 == 0:
    print('Buzz')

  else:
    print("Error: Wrong Number!!!")

else:
  print('Error: Wrong Input, Please Enter a Number!!!')
