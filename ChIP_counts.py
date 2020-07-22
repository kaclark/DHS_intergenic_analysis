import pandas as pd

DHS_ids = pd.read_csv("./data/mm10_data/DHSs/DHS_ids.bed", sep='\t', header=None, index_col=False)

all_ids = []
for row in DHS_ids[0]:
    all_ids.append(row)

ChIP_data = ["H3K27ac", "H3K4me3", "Nanog", "Oct4", "Sox2"]

for antibody in ChIP_data:
    print("Beginning count of " + antibody + "data in DHSs")
    chro = []
    start = []
    end = []
    ids = []

    direct ="data/mm10_data/ChIP/"
    path = direct + antibody + ".bed"
    data = pd.read_csv(path, sep='\t', header=None, index_col=False)

    for row in data[0]:
        chro.append(row)
    for row in data[1]:
        start.append(row)
    for row in data[2]:
        end.append(row)
    for x in range(len(chro)):
        ids.append(str(chro[x])+ ":" + str(start[x]) + "-" + str(end[x]))

    seen = []
    freq_dict = {}
    export_data = []
    for dhs in ids:
        if dhs not in seen:
            seen.append(dhs)
            freq_dict[dhs] = 1
        else:
            freq_dict[dhs] += 1
    for dhs in freq_dict.keys():
        export_data.append([dhs, freq_dict[dhs]])
    for dhs in all_ids:
        if dhs not in ids:
            export_data.append([dhs, 0])
    export = pd.DataFrame(export_data)
    export_path = direct + antibody + "_counts.csv"
    export.to_csv(export_path, index=False, header=False)



