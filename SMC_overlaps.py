#Compiles SMCs that are present in each cell count for DHS regions

#mm10_SMCs.csv generated by modification of Genome liftover of mm9_SMCs from SMC paper in SMC_id_assignment.py
#DHS_#_with_SMC.csv generated in SMC_analysis

#Exports SMC_#_filtered.csv

import pandas as pd

#load SMC data
SMC_data = pd.read_csv("data/mm10_data/SMC/mm10_SMCs.csv", header=None, index_col=False)

chr = []
start = []
end = []
id = []
for row in SMC_data[0]:
    chr.append(row)
for row in SMC_data[1]:
    start.append(row)
for row in SMC_data[2]:
    end.append(row)
for row in SMC_data[3]:
    id.append(row)

files = ['1','2','4','8']

for file in files:
    #path = "data/DHS_" + file + "_cell_with_SMC.csv"
    path = "data/mm10_data/DHS_with_SMC/DHS_" + file + "_cell_with_SMC.csv"
    with open(path) as DHS_SMCs:
        #split file into lines
        lis = [line.split() for line in DHS_SMCs] 
        for bulk in lis:
            SMC_list = []
            #Scope of the SMC data from the dhs data
            for DHS_data in bulk:
                SMCs = []
                DHS_data = DHS_data.split(',')
                DHS_removed = DHS_data[4:]
                for element in DHS_removed:
                    if len(element) > 0:
                        SMCs.append(element)
            for SMC in SMCs:
                index = id.index(SMC)
                SMC_list.append([chr[index], start[index], end[index], id[index]])
        #Keep unique data
        unique_SMC = [list(x) for x in set(tuple(x) for x in SMC_list)]
        #Export data
        SMC_df = pd.DataFrame(unique_SMC)
        print("Starting to save data for " + file + " cell")
        path = "data/mm10_data/SMC/SMC_" + file + "_filtered.csv"
        SMC_df.to_csv(path, index=False, header=False)
        print("All data for " + file + " cell successfully saved")