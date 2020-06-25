import pandas as pd

intersects = pd.read_csv("data/mm10_data/analyzed_intersects.csv", header=None, index_col=False)

intersect_ids = []
for row in intersects[0]:
    intersect_ids.append(row)

chart_rows = {}
final_data_list = []

files = ['1','2','4','8']

rows = {
    '1': [1,0,0,0],
    '2': [0,1,0,0],
    '4': [0,0,1,0],
    '8': [0,0,0,1]
}

for file in files:
    DHS_data = pd.read_csv("data/mm10_data/DHSs_intergenic_" + file + ".csv", index_col=False, header=None)

    chromosome = []
    start = []
    end = []
    
    for row in DHS_data[0]:
        chromosome.append(row)
    for row in DHS_data[1]:
        start.append(row)
    for row in DHS_data[2]:
        end.append(row)

    #all ids in this cell count
    all_ids = []
    for x in range(len(chromosome)):
        all_ids.append(str(chromosome[x]) + ":" + str(start[x]) + "-" + str(end[x]))

    for id in all_ids:
        if id not in intersect_ids:
            chart_rows[id] = rows[file]
            
for entry in chart_rows.items():
    final_data_list.append((entry[0], entry[1][0], entry[1][1], entry[1][2], entry[1][3]))
df = pd.DataFrame(final_data_list)
df.to_csv("data/mm10_data/lone_DHS_sites_chart.csv", index=False, header=False)
