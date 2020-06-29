from Bio import SeqIO
import pandas as pd

#DhS files
files = ['1','2','4','8']

for entry in files:
    seqs = []
    #Load fasta file
    for record in SeqIO.parse("data/mm10_data/DHS_" + entry + "_largest_TAD_seq.fa", "fasta"):
        seq = str(record.seq)
        seqs.append(seq)
    dataframe = pd.DataFrame(seqs)
    dataframe.to_csv("data/mm10_data/TAD_seqs_" + entry + ".csv", index=False, header=False)