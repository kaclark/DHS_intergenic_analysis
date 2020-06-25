#calculates ttests on gc content of the DHS sites

#DHS_#_gc.csv generated in calculate_gc.py

import pandas as pd
from scipy import stats

files = ['1','2','4','8']

data = []

std = []
mean = []
count = []

for entry in files:
    file_name = 'data/mm10_data/DHS_'+entry+'_gc.csv'
    gc_data = pd.read_csv(file_name)
    #Drop DHS ids
    gc_data.drop(gc_data.columns[0], 1, inplace=True)
    data.append(gc_data)


for x in range(len(data)):
    std.append(float(data[x].std(axis=0, skipna=True).values))
    mean.append(float(data[x].mean(axis=0, skipna=True).values))
    count.append(len(data[x]))

tval1_2, pval1_2 = stats.ttest_ind(data[0], data[1], axis=0, equal_var=False)
print("T value 1 cell vs 2 cell for gc content: " + str(float(tval1_2)))
print("P value 1 cell vs 2 cell for gc content: " + str(float(pval1_2)))
if(pval1_2 < 0.05):
    print("Null Hypothesis rejected for 1 cell vs 2 cell for gc content")
else:
    print("Null Hypothesis upheld for 1 cell vs 2 cell for gc content")
print("")

tval1_4, pval1_4 = stats.ttest_ind(data[0], data[2], axis=0, equal_var=False)
print("T value 1 cell vs 4 cell for gc content: " + str(float(tval1_4)))
print("P value 1 cell vs 4 cell for gc content: " + str(float(pval1_4)))
if(pval1_4 < 0.05):
    print("Null Hypothesis rejected for 1 cell vs 4 cell for gc content")
else:
    print("Null Hypothesis upheld for 1 cell vs 4 cell for gc content")
print("")

tval1_8, pval1_8 = stats.ttest_ind(data[0], data[3], axis=0, equal_var=False)
print("T value 1 cell vs 8 cell for gc content: " + str(float(tval1_8)))
print("P value 1 cell vs 8 cell for gc content: " + str(float(pval1_8)))
if(pval1_8 < 0.05):
    print("Null Hypothesis rejected for 1 cell vs 8 cell for gc content")
else:
    print("Null Hypothesis upheld for 1 cell vs 8 cell for gc content")
print("")

tval2_4, pval2_4 = stats.ttest_ind(data[1], data[2], axis=0, equal_var=False)
print("T value 2 cell vs 4 cell for gc content: " + str(float(tval2_4)))
print("P value 2 cell vs 4 cell for gc content: " + str(float(pval2_4)))
if(pval2_4 < 0.05):
    print("Null Hypothesis rejected for 2 cell vs 4 cell for gc content")
else:
    print("Null Hypothesis upheld for 2 cell vs 4 cell for gc content")
print("")

tval2_8, pval2_8 = stats.ttest_ind(data[1], data[3], axis=0, equal_var=False)
print("T value 2 cell vs 8 cell for gc content: " + str(float(tval2_8)))
print("P value 2 cell vs 8 cell for gc content: " + str(float(pval2_8)))
if(pval2_8 < 0.05):
    print("Null Hypothesis rejected for 2 cell vs 8 cell for gc content")
else:
    print("Null Hypothesis upheld for 2 cell vs 8 cell for gc content")
print("")

tval4_8, pval4_8 = stats.ttest_ind(data[2], data[3], axis=0, equal_var=False)
print("T value 4 cell vs 8 cell for gc content: " + str(float(tval4_8)))
print("P value 4 cell vs 8 cell for gc content: " + str(float(pval4_8)))
if(pval4_8 < 0.05):
    print("Null Hypothesis rejected for 4 cell vs 8 cell for gc content")
else:
    print("Null Hypothesis upheld for 4 cell vs 8 cell for gc content")
print("")