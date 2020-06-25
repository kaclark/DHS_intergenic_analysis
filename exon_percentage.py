import pandas as pd

full_gene_data_df = pd.read_csv("data/mm10_data/full_genes.csv", header=None, index_col=False)

gene_id = []
gene_length = []

gene_dict = {}

for row in full_gene_data_df[0]:
    gene_id.append(row)
for row in full_gene_data_df[4]:
    gene_length.append(row)

counter = 0
for id in gene_id:
    gene_dict[id] = gene_length[counter]
    counter += 1

exon_construct_data_df = pd.read_csv("data/mm10_data/constructed_genes.csv", header=None, index_col=False)

exon_id = []
exon_lengths = []

exon_dict = {}

for row in exon_construct_data_df[0]:
    exon_id.append(row)
for row in exon_construct_data_df[4]:
    exon_lengths.append(row)

counter = 0
for id in exon_id:
    exon_dict[id] = exon_lengths[counter]
    counter += 1

exon_percentages = []
ep_export = []

shared_ids = []
for id in gene_id:
    if id in exon_id:
        shared_ids.append(id)

for id in exon_id:
    if id not in shared_ids and id in gene_id:
        shared_ids.append(id)

for id in shared_ids:
    gene_len = gene_dict[id]
    exon_len = exon_dict[id]
    percentage = (exon_len / gene_len) * 100
    exon_percentages.append(percentage)
    ep_export.append([id, percentage])

total = 0
for perc in exon_percentages:
    total += perc
avg = total / len(exon_percentages)

print("The average mouse gene is " + str(avg) + " percent exon")
exon_percentages_df = pd.DataFrame(ep_export)
exon_construct_data_df.to_csv("data/mm10_data/exon_percentages.csv", index=False, header=False)