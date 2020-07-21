import pickle
import pandas as pd


with open("./data/groups.pickle", "rb") as pickle_in:
    groups = pickle.load(pickle_in)

in_8 = groups["in_8_only"]

TFs = ["Nanog", "Oct4", "Sox2"]

for factor in TFs:
    direct = "./data/mm10_data/ChIP/"
    import_path = direct + factor + "_counts.csv"
    data = pd.read_csv(import_path, header=None, index_col=False)
    DHS_ids_factor = []
    for row in data[0]:
        DHS_ids_factor.append(row)
    count = 0
    for dhs in in_8:
        if dhs in DHS_ids_factor:
            count += 1
    print(factor + " counts in 8 only " + str(count))

