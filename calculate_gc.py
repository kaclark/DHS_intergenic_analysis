from Bio import SeqIO
import csv

#counter = 0

files = ['1','2','4','8']

for entry in files:
    length = []
    gc_content = []
    group = []
    ids = []
    for record in SeqIO.parse("data/mm10_data/DHSs_" + entry + "_intergenic.fa", "fasta"):
        seq = str(record.seq)
        seq_len = len(seq)
        gs = seq.count('g')
        cgs = seq.count('G')
        cs = seq.count('c')
        ccs = seq.count('C')
        total = gs + cs + cgs + ccs
        gc_con = float(total)/seq_len
        gc_content.append(gc_con)
        group.append(int(entry))
        length.append(seq_len)
        ids.append(record.id)
        #counter += 1
        # if ((counter % 100) == 0):
        #     print("Current seq being analyzed: " + seq)
        #     print("Number of gs counted in seq: " + str(gs))
        #     print("Number of cs counted in seq: " + str(cs))
        #     print("Number of Gs counted in seq: " + str(cgs))
        #     print("Number of Cs counted in seq: " + str(ccs))
        #     print("Total nucleotides counted: " + str(total))
        #     print("Total nuclueotides in seq: " + str(seq_len))
        #     print("GC content: " + str(gc_con))

    # with open('data/mm10_data/DHS_'+ entry + '_GCvG.csv', mode='w') as data:
    #     data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #     for x in range(len(gc_content)):
    #         # data_writer.writerow([gc_content[x], length[x]])
    #         data_writer.writerow([gc_content[x], group[x]])

    # with open('data/mm10_data/DHS_'+ entry + '_GCvL.csv', mode='w') as data:
    #     data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #     for x in range(len(gc_content)):
    #         data_writer.writerow([gc_content[x], length[x]])
    #         #data_writer.writerow([gc_content[x], group[x]])

    # with open('data/mm10_data/DHS_'+ entry + '_lengths.csv', mode='w') as data:
    #     data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #     for x in range(len(gc_content)):
    #         # data_writer.writerow([gc_content[x], length[x]])
    #         data_writer.writerow([length[x], group[x]])

    
    with open('data/mm10_data/DHS_'+ entry + '_lengths.csv', mode='w') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for x in range(len(gc_content)):
            # data_writer.writerow([gc_content[x], length[x]])
            data_writer.writerow([ids[x], length[x]])

    with open('data/mm10_data/DHS_'+ entry + '_gc.csv', mode='w') as data:
        data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for x in range(len(gc_content)):
            # data_writer.writerow([gc_content[x], length[x]])
            data_writer.writerow([ids[x], gc_content[x]])