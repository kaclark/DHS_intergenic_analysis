#pass the directory with the partitioned DHSs in as an aurgument
# data/mm10_data/intersects/venn_partitions
import pandas as pd
import numpy as np
import pandas as pd
import sys
from pathlib import Path
from scipy.stats import mannwhitneyu

labels = []
labels_len = []
labels_gc = []
directory = sys.argv[1]
#don't use rglob
pathlist = Path(directory).rglob('*.csv')
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
    labels_len.append(name)
    labels_gc.append(name)
    gc_data.append(gc)
    len_data.append(length)
sys.stdout = open("data/mm10_data/intersects/venn_partitions/stats/wilcoxon_results.csv", "w")
print("Group 1, Group2, measurement, sum-rank, p-value, outcome")
for left in gc_data:
    for right in gc_data:
        if left != right:
            export_list = []
            index_left = gc_data.index(left)
            left_name = labels_gc[index_left]
            index_right = gc_data.index(right)
            right_name = labels_gc[index_right]
            w, p = mannwhitneyu(left, right)
            export_list.append(left_name)
            export_list.append(right_name)
            export_list.append("gc")
            export_list.append(str(w))
            export_list.append(str(p))
            if p < 0.05:
                export_list.append("rejected")
            if p > 0.05:
                export_list.append("upheld")
            export_phrase = ','.join(export_list)
            print(export_phrase)
    gc_data.remove(left)
    labels_gc.remove(left_name)

for left in len_data:
    for right in len_data:
        if left != right:
            export_list = []
            upheld = None
            index_left = len_data.index(left)
            left_name = labels_len[index_left]
            index_right = len_data.index(right)
            right_name = labels_len[index_right]
            w, p = mannwhitneyu(left, right)
            export_list.append(left_name)
            export_list.append(right_name)
            export_list.append("length")
            export_list.append(str(w))
            export_list.append(str(p))
            if p < 0.05:
                export_list.append("rejected")
            if p > 0.05:
                export_list.append("upheld")
            export_phrase = ','.join(export_list)
            print(export_phrase)
    len_data.remove(left)
    labels_len.remove(left_name)
sys.stdout.close()