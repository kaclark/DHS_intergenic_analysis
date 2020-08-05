# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import random
import subprocess

subprocess.call(["generated_shuffled_DHSs.sh"], shell=True)
#import dataset
with open('./data/jar/DHSs_onehot.pickle', 'rb') as pickle_in:
    onehot_data = pickle.load(pickle_in)
with open('./data/jar/var_chart.pickle', 'rb') as pickle_in:
    var_chart_data = pickle.load(pickle_in)
with open('./data/jar/stage_labels.pickle', 'rb') as pickle_in:
    stage_labels = pickle.load(pickle_in)
with open('./data/jar/gc.pickle', 'rb') as pickle_in:
    gc_data = pickle.load(pickle_in)
with open('./data/jar/lengths.pickle', 'rb') as pickle_in:
    length_data = pickle.load(pickle_in)
with open('./data/jar/get_group_from_dhs.pickle', 'rb') as pickle_in:
    groups_by_DHS = pickle.load(pickle_in)
with open('./data/jar/groups_trunc.pickle', 'rb') as pickle_in:
    groups_trunc = pickle.load(pickle_in)
with open('./data/jar/ng_std.pickle', 'rb') as pickle_in:
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
with open('./data/jar/in_SE.pickle', 'rb') as pickle_in:
    in_SE_data = pickle.load(pickle_in)    

sample_dataframe = pd.read_csv("data/mm10_data/DHSs/shuffled_DHSs.bed", header=None, index_col=False)
DHSs_samples = []
for row in sample_dataframe[0]:
    DHSs_samples.append(row)

#flatten seq data sequence and extend list to have rest of data
#extend lists, append single values
inputs = {}
get_DHSs = {}
dhs_index = 0
for dhs in DHSs_samples:
    #if dhs in DHSs_samples:
    input_data = []
    #for row in onehot_data[dhs]:
    #    input_data.extend(row)
    #input_data.append(gc_data[dhs])
    input_data.append(length_data[dhs])
    #input_data.append(ng_data[dhs])
    #input_data.append(H3K27ac_count_data[dhs])
    #input_data.append(H3K4me3_count_data[dhs])
    #input_data.append(Nanog_count_data[dhs])
    #input_data.append(Oct4_count_data[dhs])
    #input_data.append(Sox2_count_data[dhs])
    #input_data.append(in_SE_data[dhs])
    #add new data above this
    inputs[dhs] = input_data
    get_DHSs[dhs_index] = dhs
    dhs_index += 1
matched_list = []

# group dhs with its label
for dhs in DHSs_samples:
    matched_list.append([inputs[dhs], var_chart_data[dhs]])
    #matched_list.append([inputs[dhs], stage_labels[dhs]])
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
model.add(Dense(10, activation='relu'))
model.add(Dense(4))
model.compile(optimizer='SGD', loss='mean_squared_error',metrics=['accuracy'])
print("Model configured")

model.fit(train_data, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_data,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_data)


