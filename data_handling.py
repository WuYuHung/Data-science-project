import pandas as pd

df = pd.read_csv("raw data/Batting.csv")
index_li = list()

for index, row in df.iterrows():
    if index % 1000 == 0:
        print(index)
    if not (2005 <= row["yearID"] <= 2014 and row["G"] >= 80):
        index_li.append(index)
df = df.drop(index_li)
print(df)
df.to_csv("data/result.csv")
