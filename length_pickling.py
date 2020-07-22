import pandas as pd
import pickle

var_data = pd.read_csv("data/mm10_data/lengths/all_DHS_lengths.csv", header=None, index_col=False)

ids = []
lengths = []

for row in var_data[0]:
    ids.append(row)
for row in var_data[1]:
    lengths.append(row)

normalized_lengths = []
max_length = max(lengths)
for length in lengths:
    normalized_lengths.append(length/max_length)

print(normalized_lengths)

length_list = []

for x in range(len(ids)):
    length_list.append(normalized_lengths[x])

export_data = {}
for x in range(len(ids)):
    export_data[ids[x]] = length_list[x]

with open("./data/lengths.pickle", "wb") as pickle_out:
    pickle.dump(export_data, pickle_out)



