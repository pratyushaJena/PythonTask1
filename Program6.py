x=int(input('Enter the first number:'))
y=int(input('Enter the second number:'))
def add(a,b):
    c=a+b
    print('Addition=')
    print(c)
def substract(a,b):
    c=a-b
    print('Substraction=')
    print (c)
def multiply(a,b):
    c=a*b
    print('Multiplication=')
    print (c)
def divide(a,b):
    c=a/b
    print('Division=')
    print (c)

choice=int(input('Enter the function you want to perform:'
      ' 1 for addition'
      ' 2 for substraction'
      ' 3 for multiplication'
      ' 4 for division'))
def calculator(ch):
  if(ch==1):
    add(x,y)

  if(ch==2):
    substract(x,y)

  if(ch==3):
    multiply(x,y)

  if(ch==4):
    divide(x,y)

  if(ch<=0|ch>=5):
    print('Invalid choice')
calculator(choice)





