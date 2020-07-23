import pandas as pd
import pickle

with open('./data/jar/groups.pickle', 'rb') as pickle_in:
    groups = pickle.load(pickle_in)

state_8 = pd.read_csv("./data/mm10_data/DHSs/state_specific_8.csv", header=None, index_col=False)

state_1 = groups["in_1_only"]
state_2 = groups["in_2_only"]
state_4 = groups["in_4_only"]

state_spec = []
state_spec.extend(state_1)
state_spec.extend(state_2)
state_spec.extend(state_4)
state_spec.extend(state_8)

export_data = pd.DataFrame(state_spec)
export_data.to_csv("data/mm10_data/DHSs/state_specific_DHSs.csv", header=False, index=False)
