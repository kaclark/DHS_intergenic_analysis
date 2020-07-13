import numpy as np
import pandas as pd
import sys
from pathlib import Path

directory = sys.argv[1]
pathlist = Path(directory).rglob('*.csv')

for pre_path in pathlist:
    data_to_export = []
    ids = []
    sequences = []
    path = str(pre_path)
    csv_data = pd.read_csv(path, header=None, index_col=False)
    data = pd.DataFrame(csv_data)
    for row in data[0]:
        ids.append(">" + row)
    for row in data[1]:
        sequences.append(row)
    for x in range(len(ids)):
        data_to_export.append(ids[x])
        data_to_export.append(sequences[x])
    data_to_export_df = pd.DataFrame(data_to_export)
    pre_name = path.split('.')
    name = pre_name[0]
    export_path = name + ".fa"
    print("Saving converted file to " + export_path)
    data_to_export_df.to_csv(export_path, index=False, header=False)