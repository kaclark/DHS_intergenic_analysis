import numpy as np
import pandas as pd
import sys
from pathlib import Path

directory = sys.argv[1]
pathlist = Path(directory).rglob('*.npy')

for pre_path in pathlist:
    path = str(pre_path)
    pdy_data = np.load(path, allow_pickle=True)
    data = pd.DataFrame(pdy_data)
    pre_name = path.split('.')
    name = pre_name[0]
    export_path = name + ".bed"
    print("Saving converted file to " + export_path)
    data.to_csv(export_path, sep='\t', index=False, header=False)