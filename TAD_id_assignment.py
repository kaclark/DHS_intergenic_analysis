import pandas as pd

TAD_data = pd.read_csv("data/mm10_data/mm10_TADs.csv", header=None, index_col=False)

chr = []
start = []
end = []

TAD_id = []

TADs = []
for row in TAD_data[0]:
    chr.append(row)
for row in TAD_data[1]:
    start.append(row)
for row in TAD_data[2]:
    end.append(row)

for x in range(len(chr)):
    TAD_id.append(str(chr[x] + ":" + str(start[x]) + "-" + str(end[x])))

for x in range(len(chr)):
    TADs.append([chr[x], start[x], end[x], TAD_id[x]])

TADs_df = pd.DataFrame(TADs)
TADs_df.to_csv("data/mm10_data/mm10_TADs.csv", index=False, header=False)