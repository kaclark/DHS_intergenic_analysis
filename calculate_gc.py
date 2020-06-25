#Calculates length and GC content of DHSs sites from fasta files

#DHS_#_intergenic.fa generated from bedtools getfasta using original DHS files filtered for only intergenic regions

#Exports DHS_#_gc.csv
#Exports DHS_#_lengths.csv

from Bio import SeqIO
import csv

#DhS files
files = ['1','2','4','8']

for entry in files:
    length = []
    gc_content = []
    group = []
    ids = []
    #Load fasta file
    for record in SeqIO.parse("data/mm10_data/DHSs_" + entry + "_intergenic.fa", "fasta"):
        seq = str(record.seq)
        seq_len = len(seq)
        #count occurences of g and c in lowercase and capital forms
        gs = seq.count('g')
        cgs = seq.count('G')
        cs = seq.count('c')
        ccs = seq.count('C')
        #total base counts
        total = gs + cs + cgs + ccs
        gc_con = float(total)/seq_len
        gc_content.append(gc_con)
        length.append(seq_len)
        ids.append(record.id)

    with open('data/mm10_data/DHS_'+ entry + '_lengths.csv', mode='w') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #Add row with DHS id and sequence length
        for x in range(len(gc_content)):
            data_writer.writerow([ids[x], length[x]])

    with open('data/mm10_data/DHS_'+ entry + '_gc.csv', mode='w') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #Add row with DHS id and GC content
        for x in range(len(gc_content)):
            data_writer.writerow([ids[x], gc_content[x]])