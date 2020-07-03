#OUTDATED

#The current version of this file uses full genes and not constructed genes
#Finds nearest gene in domains that DHS intergenic site has membership in

#domains_with_full_genes_#.csv generated from gene_analsysis.py
#DHS_with_domains.csv generated in domain_analsysis.py

#Exports DHS_#_nearest_full_gene_distance.csv

import pandas as pd
import math
import time
printed = False
files = ['1', '2', '4', '8']
last_time = 0
for file in files:
    domains_with_genes = {}
    DHSs_with_domains = {}
    DHS_and_distance = []
    DHSs = []
    #path = "data/DHS_" + file + "_cell_with_domain.csv"
    #domain data doesn't have uniform columns
    printed = False
    path = "data/mm10_data/domains/domains_with_genes_" + file + ".csv"
    with open(path) as domain_genes:
        #split file into lines
        genes = []
        lis = [line.split() for line in domain_genes] 
        for bulk in lis:
            domain = None
            #Scope of the genes from the domain data
            #domain data and gene data is formatted: chr#:start-end
            #These features are being loaded from that format
            for domain_data in bulk:
                gene_list = []
                domain_data = domain_data.split(',')
                #First element is domain id
                domain = domain_data[0]
                #All remaining elements are genes or empty space
                domain_removed = domain_data[4:]
                for element in domain_removed:
                    #filter out empty space
                    if len(element) > 0:
                        genes.append(element)
            #Extract gene features and add to gene list
            for gene in genes:
                pre_chr = gene.split(':')
                chr = pre_chr[0]
                pre_loc = pre_chr[1]
                pre_start = pre_loc.split('-')
                start = pre_start[0]
                end = pre_start[1]
                #Append gene data to list of genes
                gene_list.append([chr, start, end, gene])
        #Create domain dictionary entry with genes in its scope
            domains_with_genes[domain] = gene_list
    printed = False
    path = "data/mm10_data/domains/domains_with_DHSs_" + file + ".csv"
    with open(path) as DHS_domains:
        #split file into lines
        lis = [line.split() for line in DHS_domains] 
        for bulk in lis:
            dhs_list = []
            DHS_id = None
            #Scope of the domain data from the dhs data
            for DHS_data in bulk:
                DHS = []
                data = DHS_data.split(',')
                domain_id = data[0]
                DHS_data = data[1:]
                for element in DHS_data:
                    if len(element) > 0:
                        DHSs.append(element)
            for dhs in DHSs:
                pre_chr = domain.split(':')
                chr = pre_chr[0]
                pre_loc = pre_chr[1]
                pre_start = pre_loc.split('-')
                start = pre_start[0]
                end = pre_start[1]
                dhs_list.append([chr, start, end, dhs])
            DHSs_with_domains[domain_id] = dhs_list

    printed = False
    #Find the genes that the DHS site may interact with in the domain
    for domain in DHSs_with_domains.keys():
        genes_in_domain = []
        distances = []
        on_left = []
        on_right = []
        DHS_matrix = []
        gene_matrix = domains_with_genes[domain]
        for gene in gene_matrix:
            genes_in_domain.append(gene)
        for dhs in DHSs_with_domains.values():
            DHS_matrix.append(dhs)
        for dhs_row in DHS_matrix:
            for dhs in dhs_row:
                start = int(dhs[1])
                end = int(dhs[2])
                id = dhs[3]
                #Find the center of the DHS site
                dhs_center = math.floor(( int(start) + int(end) ) / 2)
                for gene in genes_in_domain:
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
                DHS_and_distance.append([id, shortest_distance])

    #Export data
    Distance_df = pd.DataFrame(DHS_and_distance)
    path = "data/mm10_data/nearest_gene_in_domain/DHS_" + file + "_nearest_gene_in_domain_distance.csv"
    Distance_df.to_csv(path, index=False, header=False)
    time_to_complete = time.process_time() - last_time
    print("Time taken to process nearest genes for " + file + " cell: " + str(time_to_complete))
    last_time = time_to_complete
