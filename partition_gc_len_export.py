#pass the directory with the partitioned DHSs in as an aurgument
# data/mm10_data/intersects/venn_partitions
import pandas as pd
import sys
from pathlib import Path

labels = []
directory = sys.argv[1]
pathlist = Path(directory).glob('*.csv')
gc_data = []
len_data = []
for pre_path in pathlist:
    gc = []
    length = []
    path = str(pre_path)
    csv_data = pd.read_csv(path, header=None, index_col=False)
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

for lb in labels:
    index = labels.index(lb)
    export_gc_data = gc_data[index]
    export_length_data = len_data[index]
    lb_split = lb.split(':')
    name = '_'.join(lb_split)
    sys.stdout = open("data/mm10_data/intersects/venn_partitions/proc_data/gc/" + name + "_gc.csv", "w")
    for row in export_gc_data:
        print(row)
    sys.stdout.close()
    sys.stdout = open("data/mm10_data/intersects/venn_partitions/proc_data/length/" + name + "_length.csv", "w")
    for row in export_length_data:
        print(row)
    sys.stdout.close()