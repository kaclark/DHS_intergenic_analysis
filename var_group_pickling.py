import numpy as np
import pandas as pd
import sys
from pathlib import Path
import pickle

directory = sys.argv[1]
pathlist = Path(directory).glob('*.csv')
groups = {}
for pre_path in pathlist:
    DHSs = []
    path = str(pre_path)
    csv_data = pd.read_csv(path, header=None, index_col=False)
    pre_name = path.split('.')
    file_path = pre_name[0]
    name = file_path.split('\\')[-1]
    for row in csv_data[0]:
        DHSs.append(row)
    groups[name] = DHSs

with open("./data/groups.pickle", "wb") as pickle_out:
    pickle.dump(groups, pickle_out)


