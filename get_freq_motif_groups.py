import numpy as np
import pandas as pd
import sys
from pathlib import Path
import os


    
def get_freq_motif(pth):

    pre_name = path.split('.')[0]
    name = pre_name.split('\\')[-1]
    
    if os.path.getsize(pth) > 0:
        csv_data = pd.read_csv(pth, header=None, index_col=False)
        tfs = []
        for row in csv_data[1]:
            tfs.append(row)
        uq_tfs = set(tfs)
        max_hits = 0
        most_commmon_tf = "No Results"
        hit_dict = {}
        for tf in uq_tfs:
            hit_dict[tf] = tfs.count(tf)
            if tfs.count(tf) > max_hits:
                max_hits = tfs.count(tf)
                most_common_tf = tf
        tied = []
        for tf in hit_dict.keys():
            if hit_dict[tf] == max_hits:
                tied.append(tf)
        dhss = []
        for row in csv_data[0]:
            dhss.append(row)
        constr = []
        for x in range(len(tfs)):
            constr.append(dhss[x] + ":" + tfs[x])
        dhs_counts = {}
        for tf in uq_tfs:
            dhs_tf = []
            for cons in constr:
                if tf in cons:
                    dhs_tf.append(cons.split(":")[0])
            uq_dhs_in_tf = set(dhs_tf)
            dhs_counts[tf] = len(uq_dhs_in_tf)
        max_dhss = 0
        mctfd = "No Results"
        for tf in uq_tfs:
            if dhs_counts[tf] > max_dhss:
                max_dhss = dhs_counts[tf]
                mctfd = tf

        print(name + " " + str(tied) + " with " + str(max_hits) + " hits")
        csv_data = csv_data.iloc[0:0]
        max_hits = 0
        most_common_tf = "No results"
        tfs.clear()
        uq_tfs.clear()
        dhss.clear()
        constr.clear()
        dhs_counts.clear()
        dhs_tf.clear()
        max_dhss = 0
        mctfd = "No Results"
    
    else:
        print(name + " has no results")


directory = sys.argv[1]
pathlist = Path(directory).glob('*.csv')

for pre_path in pathlist:
    empty = False
    path = str(pre_path)
    get_freq_motif(path)
