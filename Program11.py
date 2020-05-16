import pandas as pd
dup = pd.read_csv(r'diamonds.csv')
lis=[]
c=0
lis=dup.duplicated(subset=None,keep='first')
print('The rows if duplicate would be indicated by "True" else "False":')
print(lis)
count=len(lis)
for i in range(count):
    if(lis[i]==True):
        c=c+1
        print('Duplicated Row')
        print(dup.loc[i])
print('The no. of duplicated rows in the diamond dataframe are:')
print(c)
if(c==0):
    print('No row is duplicated')
