import pandas as pd
import pickle

data = pd.read_csv("data/mm10_data/ChIP/Oct4_counts.csv", header=None, index_col=False)

ids = []
count = []

for row in data[0]:
    ids.append(row)
for row in data[1]:
    count.append(row)

max_count = max(count)
normalized_counts = []
for cnt in count:
    normalized_counts.append(cnt/max_count)

export_data = {}
for x in range(len(ids)):
    export_data[ids[x]] = normalized_counts[x]

with open("./data/jar/Oct4_count.pickle", "wb") as pickle_out:
    pickle.dump(export_data, pickle_out)



