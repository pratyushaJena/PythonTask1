import pandas as pd
count = pd.read_csv(r'diamonds.csv')
print(count['cut'].unique())
str = input('Enter the cut of the diamond from the above displayed list:')
lis = []
lis = count.loc[count['cut']==str,'price']
print('The prices of the diamond corresponding to the entered cut: ')
print(lis)
print('Minimum price of the diamond corresponding to the cut',end=' ')
print(str)
print(min(lis))
print('Maximum price of the diamond corresponding to the cut',end=' ')
print(str)
print(max(lis))