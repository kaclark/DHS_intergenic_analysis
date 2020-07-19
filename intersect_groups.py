<<<<<<< HEAD
from Bio import SeqIO
import pandas as pd

DHSs = []
pres_1 = []
pres_2 = []
pres_4 = []
pres_8 = []
pres_list = []

intersect_data_df = pd.read_csv("data/mm10_data/intersects/variability_chart.csv", header=None, index_col=False)
print(intersect_data_df)
for dhs in intersect_data_df[0]:
    DHSs.append(dhs)
for val in intersect_data_df[1]:
    pres_1.append(val)
for val in intersect_data_df[2]:
    pres_2.append(val)
for val in intersect_data_df[3]:
    pres_4.append(val)
for val in intersect_data_df[4]:
    pres_8.append(val)

for x in range(len(DHSs)):
    pres_list.append([DHSs[x], pres_1[x], pres_2[x], pres_4[x], pres_8[x]])

DHSs_1 = []
DHSs_2 = []
DHSs_4 = []
DHSs_8 = []

for dhs in pres_list:
    if dhs[1] == 1:
        DHSs_1.append(dhs[0])
    if dhs[2] == 1:
        DHSs_2.append(dhs[0])
    if dhs[3] == 1:
        DHSs_4.append(dhs[0])
    if dhs[4] == 1:
        DHSs_8.append(dhs[0])

#convert lists to set
in_1 = set(DHSs_1)
in_2 = set(DHSs_2)
in_4 = set(DHSs_4)
in_8 = set(DHSs_8)

in_1_2 = ["in_1_2"]
in_1_4 = ["in_1_4"]
in_1_8 = ["in_1_8"]
in_2_4 = ["in_2_4"]
in_2_8 = ["in_2_8"]
in_4_8 = ["in_4_8"]
in_1_2_4 =["in_1_2_4"] 
in_1_2_8 = ["in_1_2_8"]
in_1_4_8 = ["in_1_4_8"]
in_2_4_8 = ["in_2_4_8"]
in_1_2_4_8 =["in_1_2_4_8"] 
in_1_only = ["in_1_only"]
in_2_only = ["in_2_only"]
in_4_only =["in_4_only"]
in_8_only = ["in_8_only"]

#Get each section of a venn diagram
in_1_only_set = in_1.difference(in_2, in_4, in_8)
in_2_only_set = in_2.difference(in_1, in_4, in_8)
in_4_only_set = in_4.difference(in_1, in_2, in_8)
in_8_only_set = in_8.difference(in_1, in_2, in_4)

in_1_2_set = in_1.intersection(in_2)
in_1_2_set = in_1_2_set.difference(in_4, in_8)

in_1_4_set = in_1.intersection(in_4)
in_1_4_set = in_1_4_set.difference(in_2, in_8)

in_1_8_set = in_1.intersection(in_8)
in_1_8_set = in_1_8_set.difference(in_2, in_4)

in_2_4_set = in_2.intersection(in_4)
in_2_4_set = in_2_4_set.difference(in_1, in_8)

in_2_8_set = in_2.intersection(in_8)
in_2_8_set = in_2_8_set.difference(in_1, in_4)

in_4_8_set = in_4.intersection(in_8)
in_4_8_set = in_4_8_set.difference(in_1, in_2)

in_1_2_4_set = in_1.intersection(in_2, in_4)
in_1_2_4_set = in_1_2_4_set.difference(in_8)

in_1_2_8_set = in_1.intersection(in_2, in_8)
in_1_2_8_set = in_1_2_8_set.difference(in_4)

in_1_4_8_set = in_1.intersection(in_4, in_8)
in_1_4_8_set = in_1_4_8_set.difference(in_2)

in_2_4_8_set = in_2.intersection(in_4, in_8)
in_2_4_8_set = in_2_4_8_set.difference(in_1)

in_1_2_4_8_set = in_1.intersection(in_2, in_4, in_8)

in_1_2.extend(list(in_1_2_set))
in_1_4.extend(list(in_1_4_set))
in_1_8.extend(list(in_1_8_set))
in_2_4.extend(list(in_2_4_set))
in_2_8.extend(list(in_2_8_set))
in_4_8.extend(list(in_4_8_set))
in_1_2_4.extend(list(in_1_2_4_set))
in_1_2_8.extend(list(in_1_2_8_set))
in_1_4_8.extend(list(in_1_4_8_set))
in_2_4_8.extend(list(in_2_4_8_set))
in_1_2_4_8.extend(list(in_1_2_4_8_set)) 
in_1_only.extend(list(in_1_only_set))
in_2_only.extend(list(in_2_only_set))
in_4_only.extend(list(in_4_only_set))
in_8_only.extend(list(in_8_only_set))

partitions = [in_1_2, in_1_4, in_1_8, in_2_4, in_2_8, in_4_8, in_1_2_4, in_1_2_8, in_1_4_8, in_2_4_8, 
in_1_2_4_8, in_1_only, in_2_only, in_4_only, in_8_only]
#generate dictionary with the sequences which can be accessed by DHS id

#DHS fa files
files = ['1','2','4','8']
seq_dict = {}
for entry in files:
    #Load fasta file
    for record in SeqIO.parse("data/mm10_data/DHSs/DHSs_" + entry + "_intergenic.fa", "fasta"):
        seq_dict[record.id] = str(record.seq)

for set in partitions:
    if len(set) > 1:
        data = []
        name = set[0]
        for dhs in set:
            if dhs != name:
                data.append([dhs, seq_dict[dhs]])
        df = pd.DataFrame(data)
        path = "data/mm10_data/intersects/venn_partitions/" + name + ".csv"
        df.to_csv(path, index=False, header=False)
        print(name + " data exported to " + path)

=======
from Bio import SeqIO
import pandas as pd

DHSs = []
pres_1 = []
pres_2 = []
pres_4 = []
pres_8 = []
pres_list = []

intersect_data_df = pd.read_csv("data/mm10_data/intersects/variability_chart.csv", header=None, index_col=False)
print(intersect_data_df)
for dhs in intersect_data_df[0]:
    DHSs.append(dhs)
for val in intersect_data_df[1]:
    pres_1.append(val)
for val in intersect_data_df[2]:
    pres_2.append(val)
for val in intersect_data_df[3]:
    pres_4.append(val)
for val in intersect_data_df[4]:
    pres_8.append(val)

for x in range(len(DHSs)):
    pres_list.append([DHSs[x], pres_1[x], pres_2[x], pres_4[x], pres_8[x]])

DHSs_1 = []
DHSs_2 = []
DHSs_4 = []
DHSs_8 = []

for dhs in pres_list:
    if dhs[1] == 1:
        DHSs_1.append(dhs[0])
    if dhs[2] == 1:
        DHSs_2.append(dhs[0])
    if dhs[3] == 1:
        DHSs_4.append(dhs[0])
    if dhs[4] == 1:
        DHSs_8.append(dhs[0])

#convert lists to set
in_1 = set(DHSs_1)
in_2 = set(DHSs_2)
in_4 = set(DHSs_4)
in_8 = set(DHSs_8)

in_1_2 = ["in_1_2"]
in_1_4 = ["in_1_4"]
in_1_8 = ["in_1_8"]
in_2_4 = ["in_2_4"]
in_2_8 = ["in_2_8"]
in_4_8 = ["in_4_8"]
in_1_2_4 =["in_1_2_4"] 
in_1_2_8 = ["in_1_2_8"]
in_1_4_8 = ["in_1_4_8"]
in_2_4_8 = ["in_2_4_8"]
in_1_2_4_8 =["in_1_2_4_8"] 
in_1_only = ["in_1_only"]
in_2_only = ["in_2_only"]
in_4_only =["in_4_only"]
in_8_only = ["in_8_only"]

#Get each section of a venn diagram
in_1_only_set = in_1.difference(in_2, in_4, in_8)
in_2_only_set = in_2.difference(in_1, in_4, in_8)
in_4_only_set = in_4.difference(in_1, in_2, in_8)
in_8_only_set = in_8.difference(in_1, in_2, in_4)

in_1_2_set = in_1.intersection(in_2)
in_1_2_set = in_1_2_set.difference(in_4, in_8)

in_1_4_set = in_1.intersection(in_4)
in_1_4_set = in_1_4_set.difference(in_2, in_8)

in_1_8_set = in_1.intersection(in_8)
in_1_8_set = in_1_8_set.difference(in_2, in_4)

in_2_4_set = in_2.intersection(in_4)
in_2_4_set = in_2_4_set.difference(in_1, in_8)

in_2_8_set = in_2.intersection(in_8)
in_2_8_set = in_2_8_set.difference(in_1, in_4)

in_4_8_set = in_4.intersection(in_8)
in_4_8_set = in_4_8_set.difference(in_1, in_2)

in_1_2_4_set = in_1.intersection(in_2, in_4)
in_1_2_4_set = in_1_2_4_set.difference(in_8)

in_1_2_8_set = in_1.intersection(in_2, in_8)
in_1_2_8_set = in_1_2_8_set.difference(in_4)

in_1_4_8_set = in_1.intersection(in_4, in_8)
in_1_4_8_set = in_1_4_8_set.difference(in_2)

in_2_4_8_set = in_2.intersection(in_4, in_8)
in_2_4_8_set = in_2_4_8_set.difference(in_1)

in_1_2_4_8_set = in_1.intersection(in_2, in_4, in_8)

in_1_2.extend(list(in_1_2_set))
in_1_4.extend(list(in_1_4_set))
in_1_8.extend(list(in_1_8_set))
in_2_4.extend(list(in_2_4_set))
in_2_8.extend(list(in_2_8_set))
in_4_8.extend(list(in_4_8_set))
in_1_2_4.extend(list(in_1_2_4_set))
in_1_2_8.extend(list(in_1_2_8_set))
in_1_4_8.extend(list(in_1_4_8_set))
in_2_4_8.extend(list(in_2_4_8_set))
in_1_2_4_8.extend(list(in_1_2_4_8_set)) 
in_1_only.extend(list(in_1_only_set))
in_2_only.extend(list(in_2_only_set))
in_4_only.extend(list(in_4_only_set))
in_8_only.extend(list(in_8_only_set))

partitions = [in_1_2, in_1_4, in_1_8, in_2_4, in_2_8, in_4_8, in_1_2_4, in_1_2_8, in_1_4_8, in_2_4_8, 
in_1_2_4_8, in_1_only, in_2_only, in_4_only, in_8_only]
#generate dictionary with the sequences which can be accessed by DHS id

#DHS fa files
files = ['1','2','4','8']
seq_dict = {}
for entry in files:
    #Load fasta file
    for record in SeqIO.parse("data/mm10_data/DHSs/DHSs_" + entry + "_intergenic.fa", "fasta"):
        seq_dict[record.id] = str(record.seq)

for set in partitions:
    if len(set) > 1:
        data = []
        name = set[0]
        for dhs in set:
            if dhs != name:
                data.append([dhs, seq_dict[dhs]])
        df = pd.DataFrame(data)
        path = "data/mm10_data/intersects/venn_partitions/" + name + ".csv"
        df.to_csv(path, index=False, header=False)
        print(name + " data exported to " + path)

>>>>>>> 9d8fb6dafe577b6101dd88eb44da566e1e9170e0
