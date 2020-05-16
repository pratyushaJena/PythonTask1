list0 = []
n = int(input('Enter the size of the list'))
print('Enter the values into the list consisting of even and odd numbers')
for i in range(n):
    data=int(input())
    list0.append(data)
print('The list list0:')
print(list0)
def evenlist(list):
  j=0
  list1=[]
  list2=[]
  while(j<n):
    if(list[j] % 2 == 0):
        list1.append(list[j])
    else:
        list2.append(list[j])
    j=j+1
  list.clear()
  list.extend(list2)
  print('The list of even numbers list1=', end='')
  print(list1)
  print('The remaining list list0:', end='')
  print(list)
evenlist(list0)
print()
evenlist([1,2,3,4,5,6,7])
