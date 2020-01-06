from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
import pandas as pd
import pickle

drop_columns_test = [
    "i1",
    "i2",
    "i3",
    "playerID",
    "yearID",
    "G",
    "AB",
    "R",
    "H",
    "2B",
    "3B",
    "HR",
    "BB",
    "SO",
    "IBB",
]
drop_columns = [
    "i1",
    "i2",
    "i3",
    "i4",
    "playerID",
    "yearID",
    "G",
    "AB",
    "R",
    "H",
    "2B",
    "3B",
    "HR",
    "BB",
    "SO",
    "IBB",
]


def feature_select(raw_df, kind):
    if kind == "train":
        df = raw_df.drop(columns=drop_columns)
    if kind == "test":
        df = raw_df.drop(columns=drop_columns_test)
    return df


def PreprocessData(raw_df, kind):
    df = feature_select(raw_df, kind)
    df = df.reset_index(drop=True)
    label = df["label"].values
    df = df.drop(columns=["label", "POS"])
    # x_onehot_df = pd.get_dummies(data=df, columns=["POS"])
    ndarray = df.values
    minmax_scale = MinMaxScaler(feature_range=(0, 1))
    scaledFeatures = minmax_scale.fit_transform(ndarray)
    return scaledFeatures, label


positions = ["1B", "2B", "3B", "SS", "OF", "P", "C"]

df_test_total = list()
raw_df_test = pd.read_csv("dick data/test_POS.csv")

for pos in positions:
    temp_df = raw_df_test[raw_df_test.POS == pos]
    print(temp_df)
    df_test = PreprocessData(temp_df, kind="test")
    df_test_total.append(df_test)

print(df_test_total)

with open("df_test.pickle", "wb") as f:
    pickle.dump(df_test_total, f)

raw_df = pd.read_csv("dick data/training_POS.csv")

df_total = list()

for pos in positions:
    temp_df = raw_df[raw_df.POS == pos]
    df_test = PreprocessData(temp_df, kind="train")
    df_total.append(df_test)

with open("df.pickle", "wb") as f:
    pickle.dump(df_total, f)
