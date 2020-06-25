import time
import pandas as pd 

def duplicates(list, item):
    return [i for i, x in enumerate(list) if x == item]

panda_import_time = time.process_time()
print("pandas imported in " + str(panda_import_time))

gene_data_df = pd.read_csv("data/mm10_data/pc_genes_eo.csv", header=None, index_col=False)
gene_data_load_time = time.process_time() - panda_import_time
print("gene data loaded in " + str(gene_data_load_time))
printed = False
ids = []
path = "data/mm10_data/pc_ids_eo.csv"
with open(path) as gene_ids:
        ids_load_time = time.process_time() - gene_data_load_time
        print("gene ids loaded in " + str(ids_load_time))
        lis = [line.split() for line in gene_ids] 
        for line in lis:
            for id in line:
                id_values = id.split(',')
                for value in id_values:
                    if 'gene_id' in value:
                        ids.append(value)
id_processed_time = time.process_time() - ids_load_time
print('ids processed in ' + str(id_processed_time))

uq_ids = []
path = "data/mm10_data/uq_pc_ids_eo.csv"
uq_pc_ids_eo_df = pd.read_csv(path, header=None, index_col=False)
uq_id_load_time = time.process_time() - id_processed_time
print('unique ids loaded in ' + str(uq_id_load_time))
for row in uq_pc_ids_eo_df[0]:
    uq_ids.append(row)

chr = []
start = []
end = []

genes = []

for row in gene_data_df[0]:
    chr.append(row)
for row in gene_data_df[1]:
    start.append(row)
for row in gene_data_df[2]:
    end.append(row)

basic_gene_processed_time = time.process_time() - id_processed_time
print('basic genes processed into feature lists in ' + str(basic_gene_processed_time))
for x in range(len(chr)):
    genes.append([chr[x], start[x], end[x]])

basic_data_processed_time = time.process_time() - basic_gene_processed_time
print('basic gene data processed into gene lists ' + str(basic_gene_processed_time))


exons_in_gene = {}
for id in uq_ids:
    genes_for_id = []
    indexes = duplicates(ids, id)
    for index in indexes:
        genes_for_id.append(genes[index])
        if printed == False:
            print("Value added to genes_for_id list")
            print(genes[index])
            printed = True
    exons_in_gene[id] = genes_for_id

gene_collection_time = time.process_time() - basic_data_processed_time
print("genes collected by id in " + str(gene_collection_time))
print("Number of genes: " + str(len(exons_in_gene)))
printed = False
total = 0
constructed_genes = []
for gene_id in exons_in_gene.keys():
    total_exon_length = 0
    exon_starts = []
    exon_ends = []
    exon_start = 0
    exon_end = 0
    total += len(exons_in_gene[gene_id])
    for exon in exons_in_gene[gene_id]:
        total_exon_length += (int(exon[2]) - int(exon[1]))
        exon_starts.append(exon[1])
        exon_ends.append(exon[2])
    exon_start = min(exon_starts)
    exon_end = max(exon_ends)
    constructed_genes.append([gene_id, exon[0], exon_start, exon_end, total_exon_length])
    # if printed == False:
    #     print("Data directly given when id is accessed in dictionary:")
    #     print(exons_in_gene[key])
    #     printed = True
avg = total / len(exons_in_gene.keys())
print("Average number of exons per gene: " + str(avg))
constructed_genes_df = pd.DataFrame(constructed_genes)
path = "data/mm10_data/constructed_genes.csv"
constructed_genes_df.to_csv(path, index=False, header=False)
