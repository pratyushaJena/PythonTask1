string=input('Enter a string of combination of lower and uppercase letters')
l=len(string)
for i in range(0,l):
    if(string[i].islower()):
        print(string[i], end='')
for j in range(0,l):
    if(string[j].isupper()):
        print(string[j], end='')
