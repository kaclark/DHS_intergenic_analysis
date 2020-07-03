from Bio import motifs
import pandas as pd

motif_sentences = []

fh = open("data/tf_data/jaspar.txt")
for m in motifs.parse(fh, "jaspar"):
    motif_sentences.append([m.name, m.consensus])

df = pd.DataFrame(motif_sentences)
df.to_csv("data/tf_data/motif_sentences.csv", index=False, header=False)

