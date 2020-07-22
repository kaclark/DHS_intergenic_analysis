from Bio import SeqIO
import pickle
import pandas as pd

# one hot arrays for each nucleotide
A_oh = [1,0,0,0]
T_oh = [0,1,0,0]
G_oh = [0,0,1,0]
C_oh = [0,0,0,1]

# outcome if there is no nucleotide known for this place in the sequence
N_oh = [0,0,0,0]

matrices = {}

for record in SeqIO.parse("data/mm10_data/DHSs/extended_DHSs.fa", "fasta"):
    seq = str(record.seq).upper()
    matrix = []

    #convert nucleotides to one hot arrays and add to matrix
    for nucleotide in seq:
        if nucleotide == "A":
            matrix.append(A_oh)
        elif nucleotide == "T":
            matrix.append(T_oh)
        elif nucleotide == "G":
            matrix.append(G_oh)
        elif nucleotide == "C":
            matrix.append(C_oh)
        else:
            matrix.append(N_oh)

    matrices[record.id] = matrix

#assign DHSs their window one hot matrix
import_path = "data/mm10_data/DHSs/extended_DHSs_tracking.bed"
label_dataframe = pd.read_csv(import_path, sep='\t', header=None, index_col=False)

orig = []
windows = []

for row in label_dataframe[0]:
    orig.append(row)
for row in label_dataframe[1]:
    windows.append(row)

dhs_matrices = {}

for x in range(len(orig)):
    dhs_matrices[orig[x]] = matrices[windows[x]]

with open("./data/DHSs_onehot.pickle", "wb") as pickle_out:
    pickle.dump(dhs_matrices, pickle_out)
