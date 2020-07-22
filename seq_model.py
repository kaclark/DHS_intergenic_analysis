# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

import pickle
import random

#import dataset
with open('./data/DHSs_onehot.pickle', 'rb') as pickle_in:
    onehot_data = pickle.load(pickle_in)

with open('./data/var_chart.pickle', 'rb') as pickle_in:
    var_chart_data = pickle.load(pickle_in)

input_matched_label = {}
matched_list = []

# group dhs with its label
for dhs in onehot_data.keys():
    input_matched_label[dhs] = [onehot_data[dhs], var_chart_data[dhs]]
    matched_list.append([onehot_data[dhs], var_chart_data[dhs]])

#generate random unique indexes to pull out data for testing
testing_indexes = []
tmp_indexes = []
while(len(testing_indexes) < 500):
    tmp_indexes.append(random.randint(0,3619))
    testing_indexes = list(set(tmp_indexes))

training_indexes = []
for x in range(3618):
    if x not in testing_indexes:
        training_indexes.append(x)

training_data_list = []
training_labels_list = []

for ind in training_indexes:
    training_data_list.append(matched_list[ind][0])
    training_labels_list.append(matched_list[ind][1])

testing_data_list = []
testing_labels_list = []

for ind in testing_indexes:
    testing_data_list.append(matched_list[ind][0])
    testing_labels_list.append(matched_list[ind][1])

train_data = np.array(training_data_list)
train_labels = np.array(training_labels_list)
test_data = np.array(testing_data_list)
test_labels = np.array(testing_labels_list)

#model structure

model = Sequential()
model.add(Flatten())
model.add(Dense(300, activation='tanh'))
model.add(Dense(4))
model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(train_data, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_data,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_data)




