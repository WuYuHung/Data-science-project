import csv
import pandas as pd 
import sklearn
from sklearn import preprocessing as pp 
import numpy as np 

def feature_select(raw_df: pd.DataFrame, method: str) -> pd.DataFrame:
    """特徵選擇"""
    # TODO: 選出不要丟進去train的column，並回傳其他的column。
   #print(raw_df)
    arr = []
    if method == "data":
        for i in range (20):
            if i > 10:
                arr.append('feature' + str(i))
    df = raw_df[arr]
   #print(df)
    return df

def preprocessing(raw_df: pd.DataFrame, method: str) -> list:
    """資料預處理"""
    df = feature_select(raw_df, method)
    df = df.fillna(0)
    return df  

def main():
    """entry point"""
    raw_df = pd.read_csv("/raw data/batting.csv")
    df = preprocessing(raw_df, method="data")
    test = pd.read_csv("/raw data/test.csv")
    
    test['0']
    # TODO: 重點就在這，怎麼用training data生出prediction？ 這就有很多種方法了，反正生出一個叫prediction的2D list
    
    
    

    prediction = []
    index = test['index']
    _0 = test['0']
    _1 = test['1']
    for i in index:
        if result[_0[i]] == result[_1[i]]:
            prediction.append(1)
        else :
            prediction.append(0)
    print(prediction)
    
    with open("submit.csv", "w", newline="") as csvfile:
        # 寫檔，照這個不會錯
        spamwriter = csv.writer(
            csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL
        )
        spamwriter.writerow(["index", "ans"])
        for  index,pred in enumerate(prediction):
            spamwriter.writerow(
                [index, pred]
            )

if __name__ == "__main__":
    main()