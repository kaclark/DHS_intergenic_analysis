import pandas as pd
#because of deletions during gene uplift, this file is obsolete
starts = pd.read_csv("data/mm10_data/mm10_TADs_start.csv", header=None, index_col=False)
ends = pd.read_csv("data/mm10_data/mm10_TADs_end.csv", header=None, index_col=False)

start_chr = []
start_start = []
start_end = []
end_chr = []
end_start = []
end_end = []

TAD_id = []

TADs = []
for row in starts[0]:
    start_chr.append(row)
for row in starts[1]:
    start_start.append(row)
for row in starts[2]:
    start_end.append(row)

for row in ends[0]:
    end_chr.append(row)
for row in ends[1]:
    end_start.append(row)
for row in ends[2]:
    end_end.append(row)

for x in range(len(start_chr)):
    TAD_id.append(str(start_chr[x] + ":" + str(start_start[x]) + "-" + str(start_end[x]) + "==" + str(end_chr[x]) + ":" + str(end_start[x]) + "-" + str(end_end[x])))

for x in range(len(start_chr)):
    TADs.append([start_chr[x], start_start[x], start_end[x], end_chr[x], end_start[x], end_end[x], TAD_id[x]])

TADs_df = pd.DataFrame(TADs)
TADs_df.to_csv("data/mm10_data/mm10_TADs.csv", index=False, header=False)