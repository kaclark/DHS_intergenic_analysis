import pickle
import pandas as pd

with open("./data/groups.pickle", "rb") as pickle_in:
    groups = pickle.load(pickle_in)

print(groups["in_1_only"][0])
