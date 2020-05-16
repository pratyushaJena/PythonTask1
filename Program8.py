import pandas as pd
ser = pd.read_csv(r"diamonds.csv")
print('The list of all the columns:')
for col in ser:
    print(col)
colname = input('Enter the name of the series from above whose contents you want to see:')
print('The contents of sries',end=" ")
print(colname)
series=pd.Series(ser[colname])
print(series)
