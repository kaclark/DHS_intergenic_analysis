#OUTDATED

#Intended only for use on luria cluster. Pulls out gene types using awk upon mouse gene annoatation

#all_ids.csv generated with awk filtering for $9

#Exports gene_types_only.csv

import pandas as pd

ids = []
path = "data/mouse_gene_annotation/gene_type_investigation/all_ids.csv"
with open(path) as gene_ids:
        lis = [line.split() for line in gene_ids] 
        for line in lis:
            for id in line:
                id_values = id.split(',')
                for value in id_values:
                    if 'gene_type' in value:
                        ids.append(value)
                        
ids_df = pd.DataFrame(ids)
path = "data/mouse_gene_annotation/gene_type_investigation/gene_types_only.csv"
ids_df.to_csv(path, index=False, header=False)