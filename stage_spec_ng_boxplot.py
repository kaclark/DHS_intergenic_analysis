import pickle
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import mannwhitneyu

with open("./data/jar/stage_labels.pickle", 'rb') as pickle_in:
    stage_labels = pickle.load(pickle_in)
with open('./data/jar/ng.pickle', 'rb') as pickle_in:
    ng_data = pickle.load(pickle_in)
#stage specific
ss = []
#not stage specific
non_ss = []
for dhs in ng_data.keys():
    if stage_labels[dhs] == 1:
        ss.append(ng_data[dhs])
    elif stage_labels[dhs] == 0:
        non_ss.append(ng_data[dhs])
print(len(ss))
print(len(non_ss))
"""
print(stats.kruskal(ss, non_ss))
w, p = mannwhitneyu(ss, non_ss)
print("Rank: " + str(w))
print("Mann-Whitney p-value: " + str(p))
boxplot_data = [ss, non_ss]
labels = ["Highly Stage Specific", "Not Highly Stage Specific"]
ax = plt.axes()
ax.set_title("Nearest gene distance Stage Specificity")
fig = plt.boxplot(boxplot_data, showfliers=False)
ax.set_xticklabels(labels, fontsize=8)
plt.show()
"""



