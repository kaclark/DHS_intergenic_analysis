import pickle
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

#load DHSs by group from pickle file
#dictionary group[group_id] = DHSs_list
with open("./data/jar/groups.pickle", "rb") as pickle_in:
    groups = pickle.load(pickle_in)

import_path = "./data/mm10_data/closest_genes/all_DHSs_closest_gene_distances.csv"
data = pd.read_csv(import_path, header=None, index_col=False)

DHS_ids_cg = []
distances = []

#list to be passed to stat test
group_data = []
#get data from dataframe
for row in data[0]:
    DHS_ids_cg.append(row)
uq_DHS_ids_cg = list(set(DHS_ids_cg))
index_vals = []

for dhs in uq_DHS_ids_cg:
    index_vals.append(DHS_ids_cg.index(dhs))

for row in data[2]:
    distances.append(row)
uq_distances = []

for val in index_vals:
    uq_distances.append(distances[val])

for key in groups.keys():
    group_distances = []
    group_DHSs = groups[key]
    for dhs in group_DHSs:
        if dhs in uq_DHS_ids_cg:
            index_val = uq_DHS_ids_cg.index(dhs)
            group_distances.append(uq_distances[index_val])
        else:
            group_distances.append(0)
    group_data.append(group_distances)
print("Kruskal test results for nearest gene distance")
print(stats.kruskal(
    group_data[0],
    group_data[1],
    group_data[2],
    group_data[3],
    group_data[4],
    group_data[5],
    group_data[6],
    group_data[7],
    group_data[8],
    group_data[9],
    group_data[10],
    group_data[11],
    group_data[12]
))
labels = []
for key in groups.keys():
    pre_label = key.split('_')[1:]
    if pre_label[-1] == "only":
        pre_label.pop()
    label = ':'.join(pre_label)
    labels.append(label)
ax = plt.axes()
ax.set_title("Nearest genes of Variability Groupings")
fig = plt.boxplot(group_data)
ax.set_xticklabels(labels, fontsize=8, rotation=90)
plt.show()
