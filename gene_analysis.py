#Groups genes by SMC membership

#constructed_genes.csv generated in gene_construction.py
#SMC_#_filtered.csv generated in SMC_overlaps.py

#Exports SMC_with_50_genes.csv
#Exports SMC_with_genes_#.csv

import pandas as pd 

gene_data = []
gene_chromosomes = []
gene_start = []
gene_end = []
SMC_annotated = []
SMC_with_genes = []

exported = False

#load gene data
gene_data_df = pd.read_csv("data/mm10_data/full_genes/full_genes.csv", header=None, index_col=False)
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
    SMC_chromosomes = []
    SMC_start = []
    SMC_end = []
    SMC_id = []

    #load filtered SMC data
    SMC_data = pd.read_csv("data/mm10_data/SMC/SMC_" + file + "_filtered.csv", header=None, index_col=False)
    for row in SMC_data[0]:
        SMC_chromosomes.append(row)
    for row in SMC_data[1]:
        SMC_start.append(row)
    for row in SMC_data[2]:
        SMC_end.append(row)
    for row in SMC_data[3]:
        SMC_id.append(row)

    #construct SMCs
    SMC_groups = []
    for x in range(len(SMC_start)):
        SMC_groups.append([SMC_chromosomes[x], SMC_start[x], SMC_end[x], SMC_id[x]])

    #Process genes by chromosome
    for chrom in SMC_chromosomes:
        chrom_SMCs = []
        chrom_genes = []
        #populate the SMCs for this chromosome
        for SMC_data in SMC_groups:
            if SMC_data[0] == chrom:
                chrom_SMCs.append(SMC_data)
        #populate the genes for this chromosome
        for gene in gene_data:
            if gene[0] == chrom:
                chrom_genes.append(gene)
        #Add genes to SMCs
        for SMC in chrom_SMCs:
            gene_in_SMC = []
            entry = []
            for gene in chrom_genes:
                if int(SMC[1]) < int(gene[1]) and int(gene[2]) < int(SMC[2]):
                    gene_in_SMC.append(str(gene[0] + ":" + str(gene[1]) + "-" + str(gene[2])))
            entry.append(SMC[3])
            entry.extend(gene_in_SMC)
            SMC_with_genes.append(entry)
            #Export data for SMC with more than 50 genes for viewing in Genome Visualizer
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
                    absurd_SMC = pd.DataFrame(data_to_export)
                    absurd_SMC.to_csv("data/mm10_data/SMC/SMC_with_50_genes.csv", index=False, header=False)
                    exported = True
                    print("SMC visulaization Data exported")

    #Export data for this DHS cell count
    #Print statements are for tracking progress using slurm output file on luria cluster
    print("All data processed for " + file + " cell SMCs")
    SMC_annotated_df = pd.DataFrame(SMC_with_genes)
    print("Data has been loaded into dataframe")
    path = "data/mm10_data/SMC_with_genes/SMCs_with_genes_" + file + ".csv"
    SMC_annotated_df.to_csv(path, index=False, header=False)
    print("Data exported")


