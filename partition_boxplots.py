import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from pathlib import Path

labels = []
directory = sys.argv[1]
pathlist = Path(directory).rglob('*.csv')
gc_data = []
len_data = []
for pre_path in pathlist:
    dhs_id = []
    gc = []
    length = []
    gc_labeled = []
    len_labeled = []
    path = str(pre_path)
    csv_data = pd.read_csv(path, header=None, index_col=False)
    for id in csv_data[0]:
        dhs_id.append(id)
    for seq in csv_data[1]:
        seq_len = len(seq)
        #count occurences of g and c in lowercase and capital forms
        gs = seq.count('g')
        cgs = seq.count('G')
        cs = seq.count('c')
        ccs = seq.count('C')
        #total g and c base counts
        total = gs + cs + cgs + ccs
        seq_gc_con = float(total)/seq_len
        gc.append(seq_gc_con)
        length.append(len(seq))
    for x in range(len(dhs_id)):
        gc_labeled.append([dhs_id[x], gc[x]])
        len_labeled.append([dhs_id[x], length[x]])
    pre_name = path.split('.')
    break_slashes = pre_name[0].split('\\')
    name_filter_2 = break_slashes.pop()
    name_list = name_filter_2.split('_')
    name_list.remove("in")
    if "only" in name_list:
        name_list.remove("only")
    name = ':'.join(name_list)
    labels.append(name)
    gc_data.append(gc)
    len_data.append(length)
ax = plt.axes()
# ax.set_title("GC content of Venn Partitions")
# fig = plt.boxplot(gc_data, notch=True)
ax.set_title("Length of Venn Partitions")
fig = plt.boxplot(len_data, notch=True)
ax.set_xticklabels(labels, fontsize=8)

plt.show() 