import tensorflow
from tensorflow import keras
import csv

# Grabbing the Data for train info
train_data = []
train_key = []
test_data = []
test_key = []
with open('train2.csv', 'r') as train:
    read_train = csv.reader(train)
    r = False
    ticker = 0
    for f in read_train:
        if ticker < 22286:
            if r == False:
                r = True
            else:
                f[1] = int(f[1])
                f[2] = int(f[2])
                f[3] = float(f[3])/1587254400
                f[4] = float(f[4])
                f[5] = float(f[5])
                train_data.append(f[1:5])
                train_key.append(f[5])
            ticker += 1
        else:
            # Grabbing the Data for test info
            f[1] = int(f[1])
            f[2] = int(f[2])
            f[3] = float(f[3]) / 1587254400
            f[4] = float(f[4])
            f[5] = float(f[5])
            test_data.append(f[1:5])
            test_key.append(f[5])
            ticker += 1

# Creating the model

model = keras.Sequential()
model.add(keras.layers.Dense(4, input_shape=(4,), activation='elu'))
model.add(keras.layers.Dense(100, activation='selu'))
model.add(keras.layers.Dense(8, activation='elu'))
model.add(keras.layers.Dense(1, activation='elu'))

model.compile(optimizer="adam", loss='mean_squared_error', metrics=["accuracy"])

model.fit(train_data, train_key, epochs=30)
model.evaluate(test_data, test_key)

# prediction
predict_train = train_data[13082]
predication = model.predict([predict_train])
print(predict_train)
print("predict:" + str(predication[0]))
print(train_key[13082])
