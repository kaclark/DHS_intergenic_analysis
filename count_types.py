import pandas as pd
import csv

files = ['1','2','4','8']

def duplicates(list, item):
    return [i for i, x in enumerate(list) if x == item]

for file in files:
    #print("Intersect from " + file)
    name = "data/DHS_intersect_from_" + file + ".csv"
    DHS_data = pd.read_csv(name, header=None, index_col=False)
    chromosome = []
    start = []
    end = []
    type = []
    other_cells = []
    retain = []

    #drop redundant data
    DHS_data.drop(DHS_data.columns[5], 1, inplace=True)
    DHS_data.drop(DHS_data.columns[5], 1, inplace=True)
    DHS_data.drop(DHS_data.columns[5], 1, inplace=True)
    DHS_data.drop(DHS_data.columns[5], 1, inplace=True)

    for row in DHS_data[0]:
        chromosome.append(row)
    for row in DHS_data[1]:
        start.append(row)
    for row in DHS_data[2]:
        end.append(row)
    for row in DHS_data[3]:
        type.append(row)
    for row in DHS_data[4]:
        other_cells.append(row)


    print("Number of Intergenic sites in " + file + " cell DHS sites " + str(len(duplicates(type, "Intergenic"))))
    print("Number of Promoter sites in " + file + " cell DHS sites " + str(len(duplicates(type, "Promoter"))))
    print("Number of Interon sites in " + file + " cell DHS sites " + str(len(duplicates(type, "Intron"))))
    print("Number of Exon sites in " + file + " cell DHS sites " + str(len(duplicates(type, "Exon"))))