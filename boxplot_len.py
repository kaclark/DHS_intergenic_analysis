import pandas as pd
import matplotlib.pyplot as plt
files = ['1','2','4','8']
data = []
for entry in files:
    file_name = 'data/mm10_data/DHS_'+entry+'_lengths.csv'
    len_data = pd.read_csv(file_name)
    len_data.drop(len_data.columns[0], 1, inplace=True)
    data.append(len_data)
#looking for outliers
# counter = 0
# for cluster in data:
#     counter += 1
#     for n in cluster.itertuples():
#         if n[1] > 1000:
#             print(str(n[1]) + " " + str(counter))

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