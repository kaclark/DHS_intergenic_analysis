import pandas as pd
import pickle

var_data = pd.read_csv("data/mm10_data/closest_genes/all_DHSs_closest_gene_distances.csv", header=None, index_col=False)

ids = []
nearest_gene = []

for row in var_data[0]:
    ids.append(row)
for row in var_data[2]:
    nearest_gene.append(row)

export_data = {}
for x in range(len(ids)):
    export_data[ids[x]] = nearest_gene[x]

with open("./data/jar/ng.pickle", "wb") as pickle_out:
    pickle.dump(export_data, pickle_out)



