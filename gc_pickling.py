import pandas as pd
import pickle

var_data = pd.read_csv("data/mm10_data/gc/all_DHS_gc.csv", header=None, index_col=False)

ids = []
gcs = []

for row in var_data[0]:
    ids.append(row)
for row in var_data[1]:
    gcs.append(row)

export_data = {}
for x in range(len(ids)):
    export_data[ids[x]] = gcs[x]

with open("./data/gc.pickle", "wb") as pickle_out:
    pickle.dump(export_data, pickle_out)



