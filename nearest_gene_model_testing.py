# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
# Helper libraries
import numpy as np
import pandas as pd
import pickle
import random
import subprocess

#reshuffle sampling of 8 cell only stage dhs sites
subprocess.call(["run_eight_shuffle.sh"], shell=True)
#import dataset
with open('./data/jar/stage_labels.pickle', 'rb') as pickle_in:
    stage_labels = pickle.load(pickle_in)
with open('./data/jar/groups_trunc.pickle', 'rb') as pickle_in:
    groups_trunc = pickle.load(pickle_in)
with open('./data/jar/ng_std.pickle', 'rb') as pickle_in:
    ng_data = pickle.load(pickle_in)
DHSs_samples = []
for group in groups_trunc.keys():
    DHSs_samples.extend(groups_trunc[group])


inputs = {}
for dhs in DHSs_samples:
    input_data = []
    input_data.append(ng_data[dhs])
    inputs[dhs] = input_data
matched_list = []

ones = 0
zeros = 0
for dhs in DHSs_samples:
    if stage_labels[dhs][0] == 1:
        ones += 1
    elif stage_labels[dhs][0] == 0:
        zeros += 1
total = ones + zeros
percentage_zero = zeros/total

# group dhs with its label
for dhs in DHSs_samples:
    matched_list.append([inputs[dhs], stage_labels[dhs]])
#generate random unique indexes to pull out data for testing
testing_indexes = []
tmp_indexes = []
dhs_count = len(DHSs_samples)
testing_size = int(dhs_count/10)
while(len(testing_indexes) < testing_size):
    tmp_indexes.append(random.randint(0, dhs_count - 1))
    testing_indexes = list(set(tmp_indexes))
training_indexes = []
for x in range(dhs_count - 1):
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
model.add(Dense(5, activation='tanh'))
model.add(Dense(10, activation='softmax'))
model.add(Dense(5, activation='relu'))
model.add(Dense(2))
model.compile(optimizer='adam', loss='BinaryCrossentropy',metrics=['binary_accuracy'])

model.fit(train_data, train_labels, epochs=15)

test_loss, test_acc = model.evaluate(test_data,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)
print('Percentage Non-Stage-Specific: ' + str(percentage_zero))
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_data)
for index, val in enumerate(predictions):
    pred_perc = max(list(val))
    list_val = list(val)
    pred = [0,0]
    if list_val.index(pred_perc) == 0:
        pred = [1,0]
    else:
        pred = [0,1]
    real = testing_labels_list[index]
    correct = False
    if pred == real:
        correct = True
    print("predicition list: " + str(val) + "  Prediction: " + str(pred) + " Label:" + str(real) +  " " + str(correct))
