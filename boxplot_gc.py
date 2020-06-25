import pandas as pd
import matplotlib.pyplot as plt
files = ['1','2','4','8']
data = []
for entry in files:
    file_name = 'data/mm10_data/DHS_'+entry+'_gc.csv'
    gc_data = pd.read_csv(file_name)
    gc_data.drop(gc_data.columns[0], 1, inplace=True)
    data.append(gc_data)

fig = plt.figure();
boxplot = data[0].boxplot()
fig.savefig("visualizations/1-cell-gc-content-box-plot.png", bbox_inches="tight")
fig.clf()
boxplot = data[1].boxplot()
fig.savefig("visualizations/2-cell-gc-content-box-plot.png", bbox_inches="tight")
fig.clf()
boxplot = data[2].boxplot()
fig.savefig("visualizations/4-cell-gc-content-box-plot.png", bbox_inches="tight")
fig.clf()
boxplot = data[3].boxplot()
fig.savefig("visualizations/8-cell-gc-content-box-plot.png", bbox_inches="tight")
fig.clf()