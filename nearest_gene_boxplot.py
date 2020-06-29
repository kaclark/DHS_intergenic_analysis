import pandas as pd
import matplotlib.pyplot as plt
nearest_gene_1 = pd.read_csv("data/mm10_data/DHS_1_nearest_full_gene_distance.csv", header=None, index_col =False)
nearest_gene_2 = pd.read_csv("data/mm10_data/DHS_2_nearest_full_gene_distance.csv", header=None, index_col =False)
nearest_gene_4 = pd.read_csv("data/mm10_data/DHS_4_nearest_full_gene_distance.csv", header=None, index_col =False)
# #Drop DHS ids
# nearest_gene_1.drop(nearest_gene_1.columns[0], 1, inplace=True)
# nearest_gene_2.drop(nearest_gene_2.columns[0], 1, inplace=True)
# nearest_gene_4.drop(nearest_gene_4.columns[0], 1, inplace=True)
ng1_data = []
ng2_data = []
ng4_data = []
for row in nearest_gene_1[1]:
    ng1_data.append(int(row))
for row in nearest_gene_2[1]:
    ng2_data.append(int(row))
for row in nearest_gene_4[1]:
    ng4_data.append(int(row))
frame = [ng1_data, ng2_data, ng4_data]
plt.boxplot(frame, showfliers=False)
plt.show()