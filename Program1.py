def Add(a,b):
    def inner():
        c = a+b
        return c
    addition=inner()
    return addition+5

p=int(input('Enter the first number'))
q=int(input('Enter the second number'))
s=Add(p,q)
print('Addition after adding 5')
print(s)
