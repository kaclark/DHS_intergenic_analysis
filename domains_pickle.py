import pandas as pd
import pickle   

def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

files = ["1", "2", "4", "8"]

for file in files:
    import_path = "./data/mm10_data/domains/domains_with_DHSs_" + file + ".bed"
    data = pd.read_csv(import_path, sep="\t", header=None, index_col = False)
    TADs = {}
    tad_list = []
    tad_index = {}
    for row in data[0]:
        tad_list.append(row)
    uq_tads = set(tad_list)
    print(len(tad_list))
    print(len(uq_tads))
    for tad in uq_tads:
        tad_index[tad] = get_index_positions(tad_list, tad)
    dhs_list = []
    for row in data[1]:
        dhs_list.append(row)
    for tad in uq_tads:
        dhs_in_TAD = []
        for x in range(len(tad_index[tad])):
            dhs_in_TAD.append(dhs_list[x])
        TADs[tad] = dhs_in_TAD
    export_path = "./data/jar/domains_with_DHSs_" + file + ".pickle"
    with open(export_path, "wb") as pickle_out:
        pickle.dump(TADs, pickle_out)

    
