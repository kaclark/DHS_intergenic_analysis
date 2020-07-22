import pandas as pd
import pickle

data = pd.read_csv("data/mm10_data/ChIP/Nanog_counts.csv", header=None, index_col=False)

ids = []
count = []

for row in data[0]:
    ids.append(row)
for row in data[1]:
    count.append(row)

export_data = {}
for x in range(len(ids)):
    export_data[ids[x]] = count[x]

with open("./data/jar/Nanog_count.pickle", "wb") as pickle_out:
    pickle.dump(export_data, pickle_out)



