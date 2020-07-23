import pickle
import random

with open("./data/jar/groups.pickle", "rb") as pickle_in:
    groups = pickle.load(pickle_in)

#number of 8 only intergenic DHS sites to retain
retain = 50
indexes = []
tmp = []
#number of 8 only intergenic dhs sites
amount = 3007
while(len(indexes) < retain):
    tmp.append(random.randint(0, amount - 1))
    indexes = list(set(tmp))

sites = groups["in_8_only"]
retained = []
for ind in indexes:
    retained.append(sites[ind])

groups["in_8_only"] = retained

with open('./data/jar/groups_trunc.pickle', 'wb') as pickle_out:
    pickle.dump(groups, pickle_out)



