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