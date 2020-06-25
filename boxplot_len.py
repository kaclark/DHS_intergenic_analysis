#Saves boxplot for each cell type's length data as png

#Data generated in calculate_gc.py

#Exports #-cell-L-content-box-plot.png

import pandas as pd
import matplotlib.pyplot as plt

#Repeat for each DHS file
files = ['1','2','4','8']
data = []
for entry in files:
    file_name = 'data/mm10_data/DHS_'+entry+'_lengths.csv'
    len_data = pd.read_csv(file_name)
    #Drop DHS ids
    len_data.drop(len_data.columns[0], 1, inplace=True)
    data.append(len_data)

#Save figure for each DHS set of data
fig = plt.figure();
boxplot = data[0].boxplot()
fig.savefig("visualizations/1-cell-L-content-box-plot.png", bbox_inches="tight")
fig.clf()
boxplot = data[1].boxplot()
fig.savefig("visualizations/2-cell-L-content-box-plot.png", bbox_inches="tight")
fig.clf()
boxplot = data[2].boxplot()
fig.savefig("visualizations/4-cell-L-content-box-plot.png", bbox_inches="tight")
fig.clf()
boxplot = data[3].boxplot()
fig.savefig("visualizations/8-cell-L-content-box-plot.png", bbox_inches="tight")
fig.clf()