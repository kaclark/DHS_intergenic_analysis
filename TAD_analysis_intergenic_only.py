import pandas as pd 
import matplotlib.pyplot as plt
import csv

def duplicates(list, item):
    return [i for i, x in enumerate(list) if x == item]

chromosomes = []
chromosomes_2 = []
start1 = []
end1 = []
start2 = []
end2 = []
id = []
score = []
strand1 = []
strand2 = []
chromosome_locations = {}

TAD_data = pd.read_csv("data/mm9-TADs.csv", header=None, index_col=False)
#Get rid of header row in csv
TAD_data = TAD_data.iloc[1:]
for row in TAD_data[0]:
    chromosomes.append(row)
for row in TAD_data[1]:
    start1.append(row)
for row in TAD_data[2]:
    end1.append(row)
for row in TAD_data[3]:
    chromosomes_2.append(row)
for row in TAD_data[4]:
    start2.append(row)
for row in TAD_data[5]:
    end2.append(row)
for row in TAD_data[6]:
    id.append(row)
for row in TAD_data[7]:
    score.append(row)

#TODO: Get seq start and end data for DHS sites and group the DHS sites with their TADs
uq_chrom = set(chromosomes)
# print(uq_chrom)
for item in uq_chrom:
    chromosome_locations[item] = duplicates(chromosomes, item)
TAD_groups = []
for x in range(len(start1)):
    TAD_groups.append([chromosomes[x],end1[x], start2[x], id[x], chromosomes_2[x]])
TAD_groups_1 = {}
TAD_groups_2 = {}
TAD_groups_4 = {}
TAD_groups_8 = {}
TAD_dhs_count_1 = []
TAD_dhs_count_2 = []
TAD_dhs_count_4 = []
TAD_dhs_count_8 = []
# print(TAD_groups)
files = ['1','2','4','8']
for file in files:
    DHS_data = []
    DHS_chromosomes = []
    DHS_start = []
    DHS_end = []
    DHS_type = []
    DHS_annotated = []
    mismatched_TADs = []
    TAD_dhs_count = None
    if file == '1':
        TAD_group = TAD_groups_1
        TAD_dhs_count = TAD_dhs_count_1
    if file == '2':
        TAD_group = TAD_groups_2
        TAD_dhs_count = TAD_dhs_count_2
    if file == '4':
        TAD_group = TAD_groups_4
        TAD_dhs_count = TAD_dhs_count_4
    if file == '8':
        TAD_group = TAD_groups_8 
        TAD_dhs_count = TAD_dhs_count_8
    csv_file = "data/DHSs_" + file + ".csv"
    DHS_data_df = pd.read_csv(csv_file, header=None, index_col=False)
    retain = duplicates(DHS_data_df[3], "Intergenic")
    for index in retain:
        DHS_chromosomes.append(DHS_data_df[0][index])
        DHS_start.append(DHS_data_df[1][index])
        DHS_end.append(DHS_data_df[2][index])
    # for row in DHS_data_df[0]:
    #     DHS_chromosomes.append(row)
    # for row in DHS_data_df[1]:
    #     DHS_start.append(row)
    # for row in DHS_data_df[2]:
    #     DHS_end.append(row)
    # for row in DHS_data_df[3]:
    #     DHS_type.append(row)
    for x in range(len(DHS_chromosomes)):
        DHS_data.append([DHS_chromosomes[x], DHS_start[x], DHS_end[x]])
    # print(DHS_data)   
    for chrom in uq_chrom:
        # print("Chromosome " + str(chrom) + " in " + file +" cell")
        chrom_TADs = []
        chrom_DHSs = []
        #assigned dhs and tad history indexes should match up for searching which tad was used
        assigned = []
        tad_history = []
        #populate the tads for this chromosome
        for tad_data in TAD_groups:
            if tad_data[0] == chrom:
                if tad_data[0] == tad_data[4]:
                    chrom_TADs.append(tad_data)
                else:
                    #throw out the tads with mismatch chromosmes
                    mismatched_TADs.append(tad_data)
        for dhs_data in DHS_data:
            if dhs_data[0] == chrom:
                chrom_DHSs.append(dhs_data)
        for tad in chrom_TADs:
            dhs_in_tad = []
            for dhs in chrom_DHSs:
                if int(tad[1]) < int(dhs[1]) and int(dhs[2]) < int(tad[2]):
                    dhs_in_tad.append(dhs)
                    assigned.append(dhs)
                    tad_history.append(tad)
                    dhs.append(tad[3])
                    DHS_annotated.append(dhs)
                    
            TAD_group[tad[3]] = dhs_in_tad
            TAD_dhs_count.append(len(dhs_in_tad))
    # print(DHS_annotated)     
    # print(TAD_group)
    # print(len(DHS_annotated))
    num_of_tads = []
    for dhs in DHS_annotated:
        num_tads = len(dhs) - 3
        num_of_tads.append(num_tads)
    DHS_annotated_df = pd.DataFrame(DHS_annotated)

    # boxplot_name = "visualizations/" + file + "-cell-TAD-membership_count.png"
    # fig = plt.figure();
    # boxplot_data = pd.DataFrame(num_of_tads)
    # boxplot = boxplot_data.boxplot()
    # fig.savefig(boxplot_name, bbox_inches="tight")
    # fig.clf()

    # TAD_dataframe = pd.DataFrame(TAD_group)
    path = "data/DHS_" + file + "_cell_intergenic_with_TAD.csv"
    #DHS_annotated_df.to_csv(path, index=False, header=False)


