import pandas as pd
rc = pd.read_csv(r'diamonds.csv')
print('The original data frame:')
print(rc)
print('The total no. of rows and columns in the diamonds dataframe respectively:')
print(rc.shape)
trow = rc.shape[0]
lis = []
lis = rc.all(axis = 'columns')
print('The rows in which any value is missing will be indicated by "False" and the rows with all the values will be indicated as "True":')
print(lis)
print('The rows which has any value missing:')
for i in range(trow):
    if(lis[i]==False):
        print(rc.iloc[i])
        rc.drop([i],axis=0,inplace=True)
print('The data frame diamond after dropping the above rows:')
print(rc)

