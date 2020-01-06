import csv
import pickle

import numpy as np
from keras import regularizers
from keras.callbacks import EarlyStopping
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential

import matplotlib.pyplot as plt

with open("df.pickle", "rb") as f:
    df = pickle.load(f)
np.set_printoptions(threshold=np.inf)
print(df[0][0:5])

with open("df_test.pickle", "rb") as f:
    df_test = pickle.load(f)
print(df_test[0][0:5])

model = Sequential()

model.add(Dense(64, input_dim=12, activation="relu", kernel_initializer="uniform"))
model.add(Dropout(0.5))
model.add(Dense(32, activation="relu", kernel_initializer="uniform"))
model.add(Dropout(0.5))
model.add(Dense(16, activation="relu", kernel_initializer="uniform"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.summary()

early_stopping = EarlyStopping(monitor="val_loss", patience=15, verbose=2)

history = model.fit(
    x=df[0],
    y=df[1],
    epochs=80,
    validation_split=0.1,
    batch_size=10,
    verbose=1,
    callbacks=[early_stopping],
)

plt.plot(history.history["loss"])
plt.title("model loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
plt.show()

prediction = model.predict(x=np.array(df_test[0]), batch_size=128)

print(prediction)

mean = np.percentile(prediction, 98)
print(mean)
result = list()

for i in range(len(prediction)):
    if prediction[i] < mean:
        result.append(0)
    else:
        result.append(1)

print(prediction)

with open("predict.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["id", "ans"])
    for i in range(len(prediction)):
        spamwriter.writerow([float(i), int(result[i])])
