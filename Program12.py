import pandas as pd
diamond = pd.read_csv(r"diamonds.csv")
print('The original size of the data frame diamonds:')
print(diamond.shape)
print("75% of the given diamond's data frame rows without replacement:")
result = diamond.sample(frac=0.75, random_state=99)
print(result)
remains = []
remains = diamond.loc[~diamond.index.isin(result.index)]
remdata = pd.DataFrame(remains)
print('The other data frame with the remaining 25% of the diamond data frame :')
print(remdata)
