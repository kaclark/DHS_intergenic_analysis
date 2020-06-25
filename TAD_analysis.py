#Gathers TADs that DHS site has membership in

#mm10_TADs.csv generated by modification of Genome liftover of mm9_TADs from TAD paper in TAD_id_assignment.py
#DHS_intergenic_#.csv generated by UNKONWN

#Exports DHS_#_with_TAD.csv

import pandas as pd 
import matplotlib.pyplot as plt
import csv

printed = False
def duplicates(list, item):
    """Returns index locations of item in list"""
    return [i for i, x in enumerate(list) if x == item]

chromosomes = []
start = []
end = []
id = []
chromosome_locations = {}

#load TAD data
TAD_data = pd.read_csv("data/mm10_data/mm10_TADs.csv", header=None, index_col=False)
# #Get rid of header row in csv
# TAD_data = TAD_data.iloc[1:] -- header does not exist in mm10 file
for row in TAD_data[0]:
    chromosomes.append(row)
for row in TAD_data[1]:
    start.append(row)
for row in TAD_data[2]:
    end.append(row)
for row in TAD_data[3]:
    id.append(row)

uq_chrom = set(chromosomes)
for item in uq_chrom:
    chromosome_locations[item] = duplicates(chromosomes, item)
TAD_groups = []
for x in range(len(start)):
    TAD_groups.append([chromosomes[x],start[x], end[x], id[x]])
TAD_groups_1 = {}
TAD_groups_2 = {}
TAD_groups_4 = {}
TAD_groups_8 = {}
TAD_dhs_count_1 = []
TAD_dhs_count_2 = []
TAD_dhs_count_4 = []
TAD_dhs_count_8 = []
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
    #load DHS data
    csv_file = "data/mm10_data/DHSs_intergenic_" + file + ".csv"
    DHS_data_df = pd.read_csv(csv_file, header=None, index_col=False)
    for row in DHS_data_df[0]:
        DHS_chromosomes.append(row)
    for row in DHS_data_df[1]:
        DHS_start.append(row)
    for row in DHS_data_df[2]:
        DHS_end.append(row)
    for row in DHS_data_df[3]:
        DHS_type.append(row)
    for x in range(len(DHS_chromosomes)):
        DHS_data.append([DHS_chromosomes[x], DHS_start[x], DHS_end[x], DHS_type[x]])

    #Iterate through chromosomes
    for chrom in uq_chrom:
        chrom_TADs = []
        chrom_DHSs = []
        #populate the tads for this chromosome
        for tad_data in TAD_groups:
            if tad_data[0] == chrom:
                chrom_TADs.append(tad_data)
        #populate the dhs sites for this chromosome
        for dhs_data in DHS_data:
            if dhs_data[0] == chrom:
                chrom_DHSs.append(dhs_data)
        #For each tad, assign it to the DHS site if the DHS site is within the TAD bounds
        for tad in chrom_TADs:
            dhs_in_tad = []
            for dhs in chrom_DHSs:
                if int(tad[1]) < int(dhs[1]) and int(dhs[2]) < int(tad[2]):
                    dhs_in_tad.append(dhs)
                    dhs.append(tad[3])
                    DHS_annotated.append(dhs)
    #Export data
    DHS_annotated_df = pd.DataFrame(DHS_annotated)
    path = "data/mm10_data/DHS_" + file + "_cell_with_TAD.csv"
    DHS_annotated_df.to_csv(path, index=False, header=False)


