#Updates liftover file's conversion with the IDs of the SMCs

#mm10_SMCs.csv initially generated by liftover conversion of modified mm9_SMCs file

#Exports updated mm10_SMCs.csv

import pandas as pd

#load SMC data
SMC_data = pd.read_csv("data/mm10_data/SMC/mm10_SMCs.csv", header=None, index_col=False)

chr = []
start = []
end = []

SMC_id = []

SMCs = []
for row in SMC_data[0]:
    chr.append(row)
for row in SMC_data[1]:
    start.append(row)
for row in SMC_data[2]:
    end.append(row)

#generate ids
for x in range(len(chr)):
    SMC_id.append(str(chr[x] + ":" + str(start[x]) + "-" + str(end[x])))

#generate list of SMC data lists for dataframe
for x in range(len(chr)):
    SMCs.append([chr[x], start[x], end[x], SMC_id[x]])

#export data
SMCs_df = pd.DataFrame(SMCs)
SMCs_df.to_csv("data/mm10_data/SMC/mm10_SMCs.csv", index=False, header=False)