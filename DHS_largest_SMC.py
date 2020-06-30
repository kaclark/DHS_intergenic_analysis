import pandas as pd

DHS_longest_SMC_data = []

files = ['1','2','4','8']
printed = False
for file in files:
    #path = "data/DHS_" + file + "_cell_with_SMC.csv"
    path = "data/mm10_data/DHS_with_SMC/DHS_" + file + "_cell_with_SMC.csv"
    with open(path) as DHS_SMCs:
        #split file into lines
        lis = [line.split() for line in DHS_SMCs] 
        for bulk in lis:
            #Scope of the SMC data from the dhs data
            for DHS_data in bulk:
                SMC_list = []
                SMCs_pre_proc = []
                SMCs = []
                SMC_lengths = {}
                longest_SMC = None
                DHS_data = DHS_data.split(',')
                DHS_id = str(DHS_data[0]) + ":" + DHS_data[1] + "-" + DHS_data[2]
                DHS_removed = DHS_data[4:]
                for element in DHS_removed:
                    if len(element) > 0:
                        SMCs_pre_proc.append(element)
                for SMC in SMCs_pre_proc:
                    pre_chr = SMC.split(':')
                    chr = pre_chr[0]
                    pre_loc = pre_chr[1]
                    pre_start = pre_loc.split('-')
                    start = pre_start[0]
                    end = pre_start[1]
                    #Append SMC data to list of SMCs
                    SMCs.append([chr, start, end, SMC])
                for SMC in SMCs:
                    length = int(SMC[2]) - int(SMC[1])
                    SMC_lengths[SMC[3]] = length
                longest_len = max(SMC_lengths.values())
                for SMC in SMC_lengths.keys():
                    if SMC_lengths[SMC] == longest_len:
                        longest_SMC = SMC
                pre_chr = longest_SMC.split(':')
                chr = pre_chr[0]
                pre_loc = pre_chr[1]
                pre_start = pre_loc.split('-')
                start = pre_start[0]
                end = pre_start[1]
                DHS_longest_SMC_data.append([DHS_id, chr, start, end, longest_SMC])
    dataframe = pd.DataFrame(DHS_longest_SMC_data)
    dataframe.to_csv("data/mm10_data/DHS_" + file + "_largest_SMCs.csv", index=False, header=False)
