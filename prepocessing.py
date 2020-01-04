import csv
import pandas as pd
import sklearn
from sklearn import preprocessing as pp
import numpy as np


def feature_select(raw_df: pd.DataFrame, method: str) -> pd.DataFrame:
    """特徵選擇"""
    # TODO: 選出不要丟進去train的column，並回傳其他的column。
   # print(raw_df)
    arr = []
    if method == "data":
        for i in range(23):
            if i != 0 and i != 3 and i != 4 and i != 5 and i != 14 and i != 15 and i != 19 and i != 20 and i != 22:
                arr.append(list(raw_df)[i])

    df = raw_df[arr]
    df["AVG"] = ""
    df["OBP"] = ""
    df["SLG"] = ""
    df["OPS"] = ""
    drop_list = list()
    for index, row in df.iterrows():
        if index % 100 == 0:
            print(index)
        if row["AB"] == 0:
            drop_list.append(index)
            continue
        df["AVG"][index] = round(row["H"]/row["AB"], 3)
        df["SLG"][index] = (round((row["H"] + row["2B"] + row["3B"]
                                   * 2 + row["HR"]*3)/row["AB"], 3))
        df["OBP"][index] = (round(
            ((row["H"] + row["BB"])/(row["AB"] + row["BB"]+row["SF"])), 3))
        df["OPS"][index] = round((df["OBP"][index] + df["SLG"][index]), 3)
    df = df.drop(drop_list)
    df = df.drop(columns=["SF"])
    df.to_csv("data/calculated_data.csv")
    print(df)
    return df


def preprocessing(raw_df: pd.DataFrame, method: str) -> list:
    """資料預處理"""
    df = feature_select(raw_df, method)
    df = df
    return df
def labling(raw_df: pd.DataFrame) 
    


def main():
    """entry point"""
    raw_df = pd.read_csv("data/calculated_data.csv")
    df = preprocessing(raw_df, method="data")
    df = labling (raw_df)
    #test = pd.read_csv("data/test.csv")
    #test_df = preprocessing(test, method="data")

    # TODO: 重點就在這，怎麼用training data生出prediction？ 這就有很多種方法了，反正生出一個叫prediction的2D list


if __name__ == "__main__":
    main()
