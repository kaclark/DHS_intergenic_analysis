import pickle

with open("./data/jar/groups.pickle", "rb") as pickle_in:
    groups = pickle.load(pickle_in)

for group in groups.keys():
    print(group + " count: " + str(len(groups[group])))
