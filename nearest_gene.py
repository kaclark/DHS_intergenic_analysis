import pandas as pd
import math
import time
printed = False
# files = ['1', '2', '4', '8']
files = ['4']
last_time = 0
for file in files:
    TADs_with_genes = {}
    DHSs_with_TADs = {}
    DHS_and_distance = []
    #path = "data/DHS_" + file + "_cell_with_TAD.csv"
    path = "data/mm10_data/TADs_with_genes_" + file + ".csv"
    with open(path) as TAD_genes:
        lis = [line.split() for line in TAD_genes] 
        for bulk in lis:
            TAD = None
            #Scope of the genes from the tad data
            for TAD_data in bulk:
                gene_list = []
                genes = []
                TAD_data = TAD_data.split(',')
                TAD = TAD_data[0]
                TAD_removed = TAD_data[1:]
                for element in TAD_removed:
                    if len(element) > 0:
                        genes.append(element)
                for gene in genes:
                    pre_chr = gene.split(':')
                    chr = pre_chr[0]
                    pre_loc = pre_chr[1]
                    pre_start = pre_loc.split('-')
                    start = pre_start[0]
                    end = pre_start[1]
                    gene_list.append([chr, start, end, gene])
                TADs_with_genes[TAD] = gene_list
        # print(TADs_with_genes)
    printed = False
    path = "data/mm10_data/DHS_" + file + "_cell_with_TAD.csv"
    with open(path) as DHS_TADs:
        lis = [line.split() for line in DHS_TADs] 
        for bulk in lis:
            TAD_list = []
            DHS_id = None
            #Scope of the TAD data from the dhs data
            for DHS_data in bulk:
                TADs = []
                DHS_data = DHS_data.split(',')
                DHS_id = str(DHS_data[0]) + ":" + str(DHS_data[1]) + "-" + str(DHS_data[2])
                DHS_removed = DHS_data[4:]
                for element in DHS_removed:
                    if len(element) > 0:
                        TADs.append(element)
            for tad in TADs:
                pre_chr = tad.split(':')
                chr = pre_chr[0]
                pre_loc = pre_chr[1]
                pre_start = pre_loc.split('-')
                start = pre_start[0]
                end = pre_start[1]
                TAD_list.append([chr, start, end, tad])
            unique_TAD = [list(x) for x in set(tuple(x) for x in TAD_list)]
            DHSs_with_TADs[DHS_id] = unique_TAD

    printed = False
    for dhs in DHSs_with_TADs.keys():
        genes_in_tad = []
        distances = []
        on_left = []
        on_right = []
        for tad in DHSs_with_TADs.values():
            for gene_matrix in TADs_with_genes.values():
                for gene in gene_matrix:
                    genes_in_tad.append(gene)
        pre_chr = dhs.split(':')
        pre_loc = pre_chr[1]
        pre_start = pre_loc.split('-')
        start = int(pre_start[0])
        end = int(pre_start[1])
        dhs_center = math.floor(( int(start) + int(end) ) / 2)
        for gene in genes_in_tad:
            if int(gene[2]) < dhs_center:
                on_left.append(gene)
            elif dhs_center < int(gene[1]):
                on_right.append(gene)
        for gene in on_left:
            dis = abs(start - int(gene[2]))
            distances.append(dis)
        for gene in on_right:
            dis = abs(int(gene[1]) - end)
            distances.append(dis)
        shortest_distance = min(distances)
        DHS_and_distance.append([dhs, shortest_distance])

    Distance_df = pd.DataFrame(DHS_and_distance)
    path = "data/mm10_data/DHS_" + file + "_nearest_gene_distance.csv"
    Distance_df.to_csv(path, index=False, header=False)
    time_to_complete = time.process_time() - last_time
    print("Time taken to process nearest genes for " + file + " cell: " + str(time_to_complete))
    last_time = time_to_complete