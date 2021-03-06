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

print(stats.kruskal(ss, non_ss))
w, p = mannwhitneyu(ss, non_ss)
print("Rank: " + str(w))
print("Mann-Whitney p-value: " + str(p))
ax = plt.axes()
ax.set_title("Nearest gene distance Non-Highly Stage Specific")
plt.style.use('ggplot')
plt.xlim(0, 25000)
plt.hist(non_ss, bins=50)
plt.show()





