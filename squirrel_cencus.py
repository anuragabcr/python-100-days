import pandas as pd

df = pd.read_csv(r"data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(df.columns)
print(pd.crosstab(df['Primary Fur Color'], columns=['Primary Fur Color']))
