#Deterimines percentage similarity between genes constructed from exons and full genes 

#Full genes generated from mouse genome annoatation awk filtering
#Constructed genes generated from gene_construction.py

#Exports exon_percentages.csv

import pandas as pd

#load gene data
full_gene_data_df = pd.read_csv("data/mm10_data/full_genes.csv", header=None, index_col=False)

gene_id = []
gene_length = []

gene_dict = {}

#Add gene data to lists
for row in full_gene_data_df[0]:
    gene_id.append(row)
for row in full_gene_data_df[4]:
    gene_length.append(row)

#populate gene dict
counter = 0
for id in gene_id:
    gene_dict[id] = gene_length[counter]
    counter += 1

#load exon data
exon_construct_data_df = pd.read_csv("data/mm10_data/constructed_genes.csv", header=None, index_col=False)

exon_id = []
exon_lengths = []

exon_dict = {}

#Add exons to exon lists
for row in exon_construct_data_df[0]:
    exon_id.append(row)
for row in exon_construct_data_df[4]:
    exon_lengths.append(row)

#populate exon dict
counter = 0
for id in exon_id:
    exon_dict[id] = exon_lengths[counter]
    counter += 1

exon_percentages = []
ep_export = []

#pull out shared ids
shared_ids = []
for id in gene_id:
    if id in exon_id:
        shared_ids.append(id)

for id in exon_id:
    if id not in shared_ids and id in gene_id:
        shared_ids.append(id)

#Calculate percentage overlap
for id in shared_ids:
    gene_len = gene_dict[id]
    exon_len = exon_dict[id]
    percentage = (exon_len / gene_len) * 100
    exon_percentages.append(percentage)
    ep_export.append([id, percentage])

#Deterimine average overlap
total = 0
for perc in exon_percentages:
    total += perc
avg = total / len(exon_percentages)

print("The average mouse gene is " + str(avg) + " percent exon")
#Export data: id, percentage
exon_percentages_df = pd.DataFrame(ep_export)
exon_construct_data_df.to_csv("data/mm10_data/exon_percentages.csv", index=False, header=False)