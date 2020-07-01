import numpy as np
import pandas as pd
import sys

og_path = sys.argv[1]
file = og_path.pop()
dir = og_path
pdy_data = np.load(file)
data = pd.DataFrame(pdy_data)
name = file.split('.')[0]
export_path = dir + '/' + name + ".bed"
print("Saving converted file to " + export_path)
data.to_csv(export_path, sep='\t', comment='t', index=False)
