sub = []
mark = []
n=int(input('Enter the size  of the list sub[] and mark[]'))
print('Enter the key and then their corresponding value:')
for i in range(0,n):
    key=input()
    value=input()
    sub.append(key)
    mark.append(value)
def Dictionary(subject,markings):
  diction = dict(zip(subject,markings))
  print('The required dictionary:')
  print(diction)
  minm=min(markings)
  def getKey(dict,x):
    key=[]
    listitem=dict.items()
    for item in listitem:
        if item[1]==x:
          key.append(item[0])
          return(key)
  result=getKey(diction,minm)
  print('The key having minimum value is:')
  print(result)
Dictionary(sub,mark)
Dictionary(['physics', 'maths', 'chemistry', 'Basic electrical' ],[88,75,72,89])



