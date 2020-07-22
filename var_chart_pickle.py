import pandas as pd
import pickle

var_data = pd.read_csv("data/mm10_data/intersects/variability_chart.csv", header=None, index_col=False)

ids = []
one = []
two = []
four = []
eight = []

for row in var_data[0]:
    ids.append(row)
for row in var_data[1]:
    one.append(row)
for row in var_data[2]:
    two.append(row)
for row in var_data[3]:
    four.append(row)
for row in var_data[4]:
    eight.append(row)

var_list = []

for x in range(len(ids)):
    var_list.append([one[x], two[x], four[x], eight[x]])

export_data = {}
for x in range(len(ids)):
    export_data[ids[x]] = var_list[x]

with open("./data/var_chart.pickle", "wb") as pickle_out:
    pickle.dump(export_data, pickle_out)



