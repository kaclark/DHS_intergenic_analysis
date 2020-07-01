import numpy as np
import pandas as pd
import sys

init_path = sys.argv[1]
og_path = sys.argv[1].split('/')
file = og_path.pop()
pre_dir = og_path
# pdy_data = np.load(file)
csv_data = pd.read_csv(init_path, header=None, index_col=False)
data = pd.DataFrame(csv_data)
pre_name = file.split('.')
name = pre_name[0]
dir = '/'.join(pre_dir)
export_path = dir + '/' + name
print("Saving converted file to " + export_path + ".npy")
# data.to_csv(export_path, sep='\t', comment='t', index=False)
np.save(export_path, data)