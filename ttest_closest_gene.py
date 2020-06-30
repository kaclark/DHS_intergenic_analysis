import pandas as pd
from scipy import stats
import math

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


tval1_2, pval1_2 = stats.ttest_ind(cg1_data, cg2_data, axis=0, equal_var=False)
print("T value 1 cell vs 2 cell for closest gene: " + str(float(tval1_2)))
print("P value 1 cell vs 2 cell for closest gene: " + str(float(pval1_2)))
if(abs(pval1_2) < 0.05):
    print("Null Hypothesis rejected for 1 cell vs 2 cell for closest gene")
else:
    print("Null Hypothesis upheld for 1 cell vs 2 cell for closest gene")
print("")

tval1_4, pval1_4 = stats.ttest_ind(cg1_data, cg4_data, axis=0, equal_var=False)
print("T value 1 cell vs 4 cell for closest gene: " + str(float(tval1_4)))
print("P value 1 cell vs 4 cell for closest gene: " + str(float(pval1_4)))
if(abs(pval1_4) < 0.05):
    print("Null Hypothesis rejected for 1 cell vs 4 cell for closest gene")
else:
    print("Null Hypothesis upheld for 1 cell vs 4 cell for closest gene")
print("")

tval1_8, pval1_8 = stats.ttest_ind(cg1_data, cg8_data, axis=0, equal_var=False)
print("T value 1 cell vs 8 cell for closest gene: " + str(float(tval1_8)))
print("P value 1 cell vs 8 cell for closest gene: " + str(float(pval1_8)))
if(abs(pval1_8) < 0.05):
    print("Null Hypothesis rejected for 1 cell vs 8 cell for closest gene")
else:
    print("Null Hypothesis upheld for 1 cell vs 8 cell for closest gene")
print("")

tval2_4, pval2_4 = stats.ttest_ind(cg2_data, cg4_data, axis=0, equal_var=False)
print("T value 2 cell vs 4 cell for closest gene: " + str(float(tval2_4)))
print("P value 2 cell vs 4 cell for closest gene: " + str(float(pval2_4)))
if(abs(pval2_4) < 0.05):
    print("Null Hypothesis rejected for 2 cell vs 4 cell for closest gene")
else:
    print("Null Hypothesis upheld for 2 cell vs 4 cell for closest gene")
print("")

tval2_8, pval2_8 = stats.ttest_ind(cg2_data, cg8_data, axis=0, equal_var=False)
print("T value 2 cell vs 8 cell for closest gene: " + str(float(tval2_8)))
print("P value 2 cell vs 8 cell for closest gene: " + str(float(pval2_8)))
if(abs(pval2_8) < 0.05):
    print("Null Hypothesis rejected for 2 cell vs 8 cell for closest gene")
else:
    print("Null Hypothesis upheld for 2 cell vs 8 cell for closest gene")
print("")

tval4_8, pval4_8 = stats.ttest_ind(cg4_data, cg8_data, axis=0, equal_var=False)
print("T value 4 cell vs 8 cell for closest gene: " + str(float(tval4_8)))
print("P value 4 cell vs 8 cell for closest gene: " + str(float(pval4_8)))
if(abs(pval4_8) < 0.05):
    print("Null Hypothesis rejected for 4 cell vs 8 cell for closest gene")
else:
    print("Null Hypothesis upheld for 4 cell vs 8 cell for closest gene")
print("")