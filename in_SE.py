import pandas as pd
import pickle 

SE_data = pd.read_csv("data/mm10_data/SE/SE_intersects.csv", header=None, index_col=False)

DHS_data = pd.read_csv("data/mm10_data/DHSs/DHS_ids.bed", header=None, index_col=False)

dhs_SE = []
for row in SE_data[0]:
    dhs_SE.append(row)

all_DHSs = []
for row in DHS_data[0]:
    all_DHSs.append(row)

export_data = {}
for dhs in all_DHSs:
    if dhs in dhs_SE:
        export_data[dhs] = 1
    else:
        export_data[dhs] = 0

with open('data/jar/in_SE.pickle', 'wb') as pickle_out:
    pickle.dump(export_data, pickle_out)





