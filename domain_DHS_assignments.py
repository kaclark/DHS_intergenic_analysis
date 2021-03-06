#Gathers domains that DHS site has membership in

#mm10_domains.csv generated by modification of Genome liftover of mm9_domains from domain paper in domain_id_assignment.py
#DHS_intergenic_#.csv generated by UNKONWN

#Exports DHS_#_with_domain.csv

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

#load domain data
domain_data = pd.read_csv("data/mm10_data/domains/domains.csv", header=None, index_col=False)
# #Get rid of header row in csv
# domain_data = domain_data.iloc[1:] -- header does not exist in mm10 file
for row in domain_data[0]:
    chromosomes.append(row)
for row in domain_data[1]:
    start.append(row)
for row in domain_data[2]:
    end.append(row)
for x in range(len(chromosomes)):
    id.append(str(chromosomes[x]) + ":" + str(start[x]) + "-" + str(end[x]))
print("Domains loaded")
uq_chrom = set(chromosomes)
for item in uq_chrom:
    chromosome_locations[item] = duplicates(chromosomes, item)
domain_groups = []
for x in range(len(start)):
    domain_groups.append([chromosomes[x],start[x], end[x], id[x]])
domain_groups_1 = {}
domain_groups_2 = {}
domain_groups_4 = {}
domain_groups_8 = {}
domain_dhs_count_1 = []
domain_dhs_count_2 = []
domain_dhs_count_4 = []
domain_dhs_count_8 = []
files = ['1','2','4','8']
for file in files:
    print(file + " cell started")
    DHS_data = []
    DHS_chromosomes = []
    DHS_start = []
    DHS_end = []
    DHS_type = []
    mismatched_domains = []
    domain_dhs_count = None
    domains = []
    if file == '1':
        domain_group = domain_groups_1
        domain_dhs_count = domain_dhs_count_1
    if file == '2':
        domain_group = domain_groups_2
        domain_dhs_count = domain_dhs_count_2
    if file == '4':
        domain_group = domain_groups_4
        domain_dhs_count = domain_dhs_count_4
    if file == '8':
        domain_group = domain_groups_8 
        domain_dhs_count = domain_dhs_count_8
    #load DHS data
    #TODO: Find where this is before rerunning
    csv_file = "data/mm10_data/DHSs/DHSs_intergenic_" + file + ".csv"
    DHS_data_df = pd.read_csv(csv_file, header=None, index_col=False)
    for row in DHS_data_df[0]:
        DHS_chromosomes.append(row)
    for row in DHS_data_df[1]:
        DHS_start.append(row)
    for row in DHS_data_df[2]:
        DHS_end.append(row)
    for x in range(len(DHS_chromosomes)):
        DHS_data.append([DHS_chromosomes[x], DHS_start[x], DHS_end[x], str(DHS_chromosomes[x]) + ":" + str(DHS_start[x]) + "-" + str(DHS_end[x])])
    print("DHS data loaded")
    #Iterate through chromosomes
    for chrom in uq_chrom:
        chrom_domains = []
        chrom_DHSs = []
        #populate the domains for this chromosome
        for domain_data in domain_groups:
            if domain_data[0] == chrom:
                chrom_domains.append(domain_data)
        #populate the dhs sites for this chromosome
        for dhs_data in DHS_data:
            if dhs_data[0] == chrom:
                chrom_DHSs.append(dhs_data)
        #For each domain, assign it to the DHS site if the DHS site is within the domain bounds
        for domain in chrom_domains:
            dhs_in_domain = []
            local_domain_list = [domain[3]]
            for dhs in chrom_DHSs:
                if int(domain[1]) < int(dhs[1]) and int(dhs[2]) < int(domain[2]):
                    dhs_in_domain.append(dhs[3])
            local_domain_list.extend(dhs_in_domain)
            if len(dhs_in_domain) > 0:
                domains.append(local_domain_list)
    print("DHSs grouped")
    #Export data
    domain_annotated_df = pd.DataFrame(domains)
    path = "data/mm10_data/domains/domains_with_DHSs_" + file + ".csv"
    domain_annotated_df.to_csv(path, index=False, header=False)
    print("Data exported for " + file + " cell")


