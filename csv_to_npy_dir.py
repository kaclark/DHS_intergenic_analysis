import numpy as np
import pandas as pd
import sys
from pathlib import Path

directory = sys.argv[1]
pathlist = Path(directory).rglob('*.csv')

for pre_path in pathlist:
    path = str(pre_path)
    csv_data = pd.read_csv(path, header=None, index_col=False)
    data = pd.DataFrame(csv_data)
    pre_name = path.split('.')
    name = pre_name[0]
    export_path = name + ".npy"
    print("Saving converted file to " + export_path)   
    np.save(export_path, data)  