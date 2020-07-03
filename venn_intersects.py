from venn import venn
import pandas as pd
import matplotlib.pyplot as plt

DHSs = []
pres_1 = []
pres_2 = []
pres_4 = []
pres_8 = []
pres_list = []

intersect_data_df = pd.read_csv("data/mm10_data/intersects/variability_chart.csv", header=None, index_col=False)
print(intersect_data_df)
for dhs in intersect_data_df[0]:
    DHSs.append(dhs)
for val in intersect_data_df[1]:
    pres_1.append(val)
for val in intersect_data_df[2]:
    pres_2.append(val)
for val in intersect_data_df[3]:
    pres_4.append(val)
for val in intersect_data_df[4]:
    pres_8.append(val)

for x in range(len(DHSs)):
    pres_list.append([DHSs[x], pres_1[x], pres_2[x], pres_4[x], pres_8[x]])

DHSs_1 = []
DHSs_2 = []
DHSs_4 = []
DHSs_8 = []

for dhs in pres_list:
    if dhs[1] == 1:
        DHSs_1.append(dhs[0])
    if dhs[2] == 1:
        DHSs_2.append(dhs[0])
    if dhs[3] == 1:
        DHSs_4.append(dhs[0])
    if dhs[4] == 1:
        DHSs_8.append(dhs[0])

states = {}
in_1 = set(DHSs_1)
in_2 = set(DHSs_2)
in_4 = set(DHSs_4)
in_8 = set(DHSs_8)

states["1 cell"] = in_1
states["2 cell"] = in_2
states["4 cell"] = in_4
states["8 cell"] = in_8

venn(states)
plt.show()