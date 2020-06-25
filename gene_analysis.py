#Groups genes by TAD membership

#constructed_genes.csv generated in gene_construction.py
#TAD_#_filtered.csv generated in TAD_overlaps.py

#Exports TAD_with_50_genes.csv
#Exports TAD_with_genes_#.csv

import pandas as pd 

gene_data = []
gene_chromosomes = []
gene_start = []
gene_end = []
TAD_annotated = []
TAD_with_genes = []

exported = False

#load gene data
gene_data_df = pd.read_csv("data/mm10_data/constructed_genes.csv", header=None, index_col=False)
#Add gene data to gene lists
for row in gene_data_df[1]:
    gene_chromosomes.append(row)
for row in gene_data_df[2]:
    gene_start.append(row)
for row in gene_data_df[3]:
    gene_end.append(row)
for x in range(len(gene_chromosomes)):
    gene_data.append([gene_chromosomes[x], gene_start[x], gene_end[x]])

#DHS cell counts
files = ['1','2','4','8']

for file in files:
    tad_chromosomes = []
    tad_start = []
    tad_end = []
    tad_id = []

    #load filtered TAD data
    TAD_data = pd.read_csv("data/mm10_data/TAD_" + file + "_filtered.csv", header=None, index_col=False)
    for row in TAD_data[0]:
        tad_chromosomes.append(row)
    for row in TAD_data[1]:
        tad_start.append(row)
    for row in TAD_data[2]:
        tad_end.append(row)
    for row in TAD_data[3]:
        tad_id.append(row)

    #construct TADs
    TAD_groups = []
    for x in range(len(tad_start)):
        TAD_groups.append([tad_chromosomes[x], tad_start[x], tad_end[x], tad_id[x]])

    #Process genes by chromosome
    for chrom in tad_chromosomes:
        chrom_TADs = []
        chrom_genes = []
        #populate the tads for this chromosome
        for tad_data in TAD_groups:
            if tad_data[0] == chrom:
                chrom_TADs.append(tad_data)
        #populate the genes for this chromosome
        for gene in gene_data:
            if gene[0] == chrom:
                chrom_genes.append(gene)
        #Add genes to TADs
        for tad in chrom_TADs:
            gene_in_tad = []
            entry = []
            for gene in chrom_genes:
                if int(tad[1]) < int(gene[1]) and int(gene[2]) < int(tad[2]):
                    gene_in_tad.append(str(gene[0] + ":" + str(gene[1]) + "-" + str(gene[2])))
            entry.append(tad[3])
            entry.extend(gene_in_tad)
            TAD_with_genes.append(entry)
            #Export data for TAD with more than 50 genes for viewing in Genome Visualizer
            if len(entry) > 50:
                data_to_export = []
                if exported == False:
                    for value in entry:
                        pre_chr = value.split(':')
                        chr = pre_chr[0]
                        pre_loc = pre_chr[1]
                        pre_start = pre_loc.split('-')
                        start = pre_start[0]
                        end = pre_start[1]
                        data_to_export.append([chr, start, end])
                    absurd_TAD = pd.DataFrame(data_to_export)
                    absurd_TAD.to_csv("data/mm10_data/TAD_with_50_genes.csv", index=False, header=False)
                    exported = True
                    print("TAD visulaization Data exported")

    #Export data for this DHS cell count
    #Print statements are for tracking progress using slurm output file on luria cluster
    print("All data processed for " + file + " cell TADs")
    tad_annotated_df = pd.DataFrame(TAD_with_genes)
    print("Data has been loaded into dataframe")
    path = "data/mm10_data/TADs_with_genes_" + file + ".csv"
    tad_annotated_df.to_csv(path, index=False, header=False)
    print("Data exported")


