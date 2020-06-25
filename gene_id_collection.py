#Exports list of gene ids

#pc_ids_eo.csv generated by awk filtering of mouse gene annoatation for protein_coding, exon_number, chr, with # lines removed for column $9

#Exports gene_ids_only.csv

import pandas as pd

ids = []
path = "data/mm10_data/pc_ids_eo.csv"
with open(path) as gene_ids:
        lis = [line.split() for line in gene_ids] 
        for line in lis:
            for id in line:
                id_values = id.split(',')
                for value in id_values:
                    if 'gene_id' in value:
                        ids.append(value)
                        
ids_df = pd.DataFrame(ids)
path = "data/mm10_data/gene_ids_only.csv"
ids_df.to_csv(path, index=False, header=False)