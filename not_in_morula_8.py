import pandas as pd
import pickle

morula_data = pd.read_csv("data/mm10_data/DHSs/morula_ids.bed", header=None, index_col=False)
m_ids = []

for row in morula_data[0]:
    m_ids.append(row)

with open('./data/jar/groups.pickle', 'rb') as pickle_in:
    groups = pickle.load(pickle_in)

in_8 = groups["in_8_only"]

state_specific = []
for dhs in in_8:
    if dhs not in m_ids:
        state_specific.append(dhs)

export_data = pd.DataFrame(state_specific)
export_data.to_csv("data/mm10_data/DHSs/state_specific_8.csv", index=False, header=False)
