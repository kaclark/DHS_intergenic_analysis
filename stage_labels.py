import pandas as pd
import pickle

DHS_dataframe = pd.read_csv("data/mm10_data/DHSs/DHS_ids.bed", header=None, index_col=False)
all_DHSs = []
for row in DHS_dataframe[0]:
    all_DHSs.append(row)
stage_spec_dataframe = pd.read_csv("data/mm10_data/DHSs/stage_specific_DHSs.csv", header=None, index_col=False)
stage_spec = []
for row in stage_spec_dataframe[0]:
    stage_spec.append(row)
stage_spec_labels_dict = {}
for dhs in all_DHSs:
    if dhs in stage_spec:
        stage_spec_labels_dict[dhs] = [1,0]
    else:
        stage_spec_labels_dict[dhs] = [0,1]
print(len(stage_spec_labels_dict.keys()))
with open('./data/jar/stage_labels.pickle', 'wb') as pickle_out:
    pickle.dump(stage_spec_labels_dict, pickle_out)
