import pandas as pd

DHS_longest_TAD_data = []

files = ['1','2','4','8']
printed = False
for file in files:
    #path = "data/DHS_" + file + "_cell_with_TAD.csv"
    path = "data/mm10_data/DHS_" + file + "_cell_with_TAD.csv"
    with open(path) as DHS_TADs:
        #split file into lines
        lis = [line.split() for line in DHS_TADs] 
        for bulk in lis:
            #Scope of the TAD data from the dhs data
            for DHS_data in bulk:
                TAD_list = []
                TADs_pre_proc = []
                TADs = []
                TAD_lengths = {}
                longest_TAD = None
                DHS_data = DHS_data.split(',')
                DHS_id = str(DHS_data[0]) + ":" + DHS_data[1] + "-" + DHS_data[2]
                DHS_removed = DHS_data[4:]
                for element in DHS_removed:
                    if len(element) > 0:
                        TADs_pre_proc.append(element)
                for tad in TADs_pre_proc:
                    pre_chr = tad.split(':')
                    chr = pre_chr[0]
                    pre_loc = pre_chr[1]
                    pre_start = pre_loc.split('-')
                    start = pre_start[0]
                    end = pre_start[1]
                    #Append TAD data to list of TADs
                    TADs.append([chr, start, end, tad])
                for tad in TADs:
                    length = int(tad[2]) - int(tad[1])
                    TAD_lengths[tad[3]] = length
                longest_len = max(TAD_lengths.values())
                for tad in TAD_lengths.keys():
                    if TAD_lengths[tad] == longest_len:
                        longest_TAD = tad
                pre_chr = longest_TAD.split(':')
                chr = pre_chr[0]
                pre_loc = pre_chr[1]
                pre_start = pre_loc.split('-')
                start = pre_start[0]
                end = pre_start[1]
                DHS_longest_TAD_data.append([DHS_id, chr, start, end, longest_TAD])
    dataframe = pd.DataFrame(DHS_longest_TAD_data)
    dataframe.to_csv("data/mm10_data/DHS_" + file + "_largest_TADs.csv", index=False, header=False)
