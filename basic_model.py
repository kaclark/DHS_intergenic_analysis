# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

import pickle
import random

#import dataset
with open('./data/jar/DHSs_onehot.pickle', 'rb') as pickle_in:
    onehot_data = pickle.load(pickle_in)
print("onehot data loaded")
with open('./data/jar/var_chart.pickle', 'rb') as pickle_in:
    var_chart_data = pickle.load(pickle_in)
print("var chart data loaded")
with open('./data/jar/gc.pickle', 'rb') as pickle_in:
    gc_data = pickle.load(pickle_in)
print("gc data loaded")
with open('./data/jar/lengths.pickle', 'rb') as pickle_in:
    length_data = pickle.load(pickle_in)
print("length data loaded")
with open('./data/jar/get_group_from_dhs.pickle', 'rb') as pickle_in:
    groups_by_DHS = pickle.load(pickle_in)
with open('./data/jar/groups_trunc.pickle', 'rb') as pickle_in:
    groups_trunc = pickle.load(pickle_in)
with open('./data/jar/ng.pickle', 'rb') as pickle_in:
    ng_data = pickle.load(pickle_in)
with open('./data/jar/H3K27ac_count.pickle', 'rb') as pickle_in:
    H3K27ac_count_data = pickle.load(pickle_in)
with open('./data/jar/H3K4me3_count.pickle', 'rb') as pickle_in:
    H3K4me3_count_data = pickle.load(pickle_in)
with open('./data/jar/Nanog_count.pickle', 'rb') as pickle_in:
    Nanog_count_data = pickle.load(pickle_in)
with open('./data/jar/Oct4_count.pickle', 'rb') as pickle_in:
    Oct4_count_data = pickle.load(pickle_in)
with open('./data/jar/Sox2_count.pickle', 'rb') as pickle_in:
    Sox2_count_data = pickle.load(pickle_in)

#DHSs_samples = []
#for group in groups_trunc.keys():
#    DHSs_samples.extend(groups_trunc[group])

#flatten seq data sequence and extend list to have rest of data
#extend lists, append single values
inputs = {}
get_DHSs = {}
dhs_index = 0
for dhs in onehot_data.keys():
    #if dhs in DHSs_samples:
    input_data = []
    for row in onehot_data[dhs]:
        input_data.extend(row)
    input_data.append(gc_data[dhs])
    input_data.append(length_data[dhs])
    input_data.append(ng_data[dhs])
    input_data.append(H3K27ac_count_data[dhs])
    input_data.append(H3K4me3_count_data[dhs])
    input_data.append(Nanog_count_data[dhs])
    input_data.append(Oct4_count_data[dhs])
    input_data.append(Sox2_count_data[dhs])
    inputs[dhs] = input_data
    get_DHSs[dhs_index] = dhs
    dhs_index += 1
print("input data collected")
matched_list = []

# group dhs with its label
for dhs in onehot_data.keys():
    matched_list.append([inputs[dhs], var_chart_data[dhs]])
print("input data matched to labels")

#generate random unique indexes to pull out data for testing
testing_indexes = []
tmp_indexes = []
testing_size = 100
dhs_count = len(onehot_data.keys())
while(len(testing_indexes) < testing_size):
    tmp_indexes.append(random.randint(0, dhs_count - 1))
    testing_indexes = list(set(tmp_indexes))
print("Testing index selected")
training_indexes = []
for x in range(dhs_count - 1):
    if x not in testing_indexes:
        training_indexes.append(x)
print("Training index selected")
training_data_list = []
training_labels_list = []

for ind in training_indexes:
    training_data_list.append(matched_list[ind][0])
    training_labels_list.append(matched_list[ind][1])
print("Training data collected")

testing_data_list = []
testing_labels_list = []

for ind in testing_indexes:
    testing_data_list.append(matched_list[ind][0])
    testing_labels_list.append(matched_list[ind][1])
print("Testing data collected")

train_data = np.array(training_data_list)
train_labels = np.array(training_labels_list)
print("Training data formatted")
test_data = np.array(testing_data_list)
test_labels = np.array(testing_labels_list)
print("Testing data formatted")

#model structure

model = Sequential()
model.add(Dense(300, activation='tanh'))
model.add(Dense(4))
model.compile(optimizer='SGD', loss='mean_squared_error',metrics=['accuracy'])
print("Model configured")

model.fit(train_data, train_labels, epochs=100)

test_loss, test_acc = model.evaluate(test_data,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_data)
print(model.summary())
"""
#tally up how what number of the testing data were in which group
testing_data_group_freq = {}
for ind in testing_indexes:
    dhs = get_DHSs[ind]
    group = groups_by_DHS[dhs]
    if group not in testing_data_group_freq:
        testing_data_group_freq[group] = 1
    else:
        testing_data_group_freq[group] += 1

#get percentages of testing data per group
for group in testing_data_group_freq.keys():
    print(group + " percentage in testing data: " + str((testing_data_group_freq[group]/testing_size)*100))
"""



