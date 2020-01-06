import pandas as pd

test_label = pd.read_csv("dick data/test_POS.csv")["label"]

predict_df = pd.read_csv("predict.csv")["ans"]

length = len(test_label)
sucess = 0
label_1 = 0
scoring_label_1 = 0

label_0 = 0
scoring_label_0 = 0

for i, j in zip(test_label, predict_df):
    if i == j:
        sucess += 1
    if i == j and i == 1:
        scoring_label_1 += 1
    if j == 1:
        label_1 += 1
    if i == j and i == 0:
        scoring_label_0 += 1
    if j == 0:
        label_0 += 1

print("scoring: ", sucess / length)
print("label = 1 amount: ", label_1)
print("scoring in label = 1: ", scoring_label_1 / label_1)
print("label = 0 amount: ", label_0)
print("scoring in label = 0: ", scoring_label_0 / label_0)
