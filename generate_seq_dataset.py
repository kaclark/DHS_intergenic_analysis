import pickle
import numpy as np

with open("./data/DHSs_onehot.pickle", "rb") as pickle_in:
    import_data = pickle.load(pickle_in)

data = []
for dhs in import_data.keys():
    data.append(import_data[dhs])

np_data = np.asarray(data)
print(np_data.shape)
