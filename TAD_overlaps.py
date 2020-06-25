import pandas as pd

TAD_data = pd.read_csv("data/mm10_data/mm10_TADs.csv", header=None, index_col=False)

chr = []
start = []
end = []
id = []
for row in TAD_data[0]:
    chr.append(row)
for row in TAD_data[1]:
    start.append(row)
for row in TAD_data[2]:
    end.append(row)
for row in TAD_data[3]:
    id.append(row)

files = ['1','2','4','8']

for file in files:
    #path = "data/DHS_" + file + "_cell_with_TAD.csv"
    path = "data/mm10_data/DHS_" + file + "_cell_with_TAD.csv"
    with open(path) as DHS_TADs:
        lis = [line.split() for line in DHS_TADs] 
        for bulk in lis:
            
            #Scope of the TAD data from the dhs data
            for DHS_data in bulk:
                TADs = []
                DHS_data = DHS_data.split(',')
                DHS_removed = DHS_data[4:]
                for element in DHS_removed:
                    if len(element) > 0:
                        TADs.append(element)
            for tad in TADs:
                index = id.index(tad)
                TAD_list.append([chr[index], start[index], end[index], id[index]])
        unique_TAD = [list(x) for x in set(tuple(x) for x in TAD_list)]
        TAD_df = pd.DataFrame(unique_TAD)
        print("Starting to save data for " + file + " cell")
        #path = "data/TAD_" + file + "_filtered.csv"
        path = "data/mm10_data/TAD_" + file + "_filtered.csv"
        TAD_df.to_csv(path, index=False, header=False)
        print("All data for " + file + " cell successfully saved")