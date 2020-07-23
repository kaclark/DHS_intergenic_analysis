import pandas as pd
import matplotlib.pyplot as plt
nearest_gene_1 = pd.read_csv("data/mm10_data/closest_genes/closest_gene_distances_1.csv", header=None, index_col =False)
nearest_gene_2 = pd.read_csv("data/mm10_data/closest_genes/closest_gene_distances_2.csv", header=None, index_col =False)
nearest_gene_4 = pd.read_csv("data/mm10_data/closest_genes/closest_gene_distances_4.csv", header=None, index_col =False)
nearest_gene_8 = pd.read_csv("data/mm10_data/closest_genes/closest_gene_distances_8.csv", header=None, index_col =False)

cg1_data = []
cg2_data = []
cg4_data = []
cg8_data = []
for row in nearest_gene_1[2]:
    cg1_data.append(int(row))
for row in nearest_gene_2[2]:
    cg2_data.append(int(row))
for row in nearest_gene_4[2]:
    cg4_data.append(int(row))
for row in nearest_gene_8[2]:
    cg8_data.append(int(row))
frame = [cg1_data, cg2_data, cg4_data, cg8_data]
plt.boxplot(frame, showfliers=False)
plt.show()
