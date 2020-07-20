import pickle
import pandas as pd
from scipy import stats

#load DHSs by group from pickle file
#dictionary group[group_id] = DHSs_list
with open("./data/groups.pickle", "rb") as pickle_in:
    groups = pickle.load(pickle_in)

#ChIP_data_antigens
ChIP_data = ["H3K27ac", "H3K4me3", "Nanog", "Sox2", "Oct4"]
#For each antigen
for antibody in ChIP_data:
    direct = "./data/mm10_data/ChIP/"
    import_path = direct + antibody + "_counts.csv"
    data = pd.read_csv(import_path, header=None, index_col=False)
    DHS_ids_antibody = []
    #comes from antibody data
    counts = []

    if antibody == "Nanog":
        print(antibody)

    #list to be passed to stat test
    group_data = []
    #get data from dataframe
    for row in data[0]:
        DHS_ids_antibody.append(row)
    for row in data[1]:
        counts.append(row)

    for key in groups.keys():
        group_counts = []
        group_DHSs = groups[key]

        for dhs in group_DHSs:
            if dhs in DHS_ids_antibody:
                index_val = DHS_ids_antibody.index(dhs)
                group_counts.append(counts[index_val])
            else:
                group_counts.append(0)
        group_data.append(group_counts)
    #print(group_data)
    #print(antibody)
    #print(group_data)
    print("Kruskal test results for " + antibody)
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
