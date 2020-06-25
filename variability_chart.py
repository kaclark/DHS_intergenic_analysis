import pandas as pd
import csv

files = ['1','2','4','8']
final_data_dict = {}
final_data_list = []

for file in files:
    #print("Intersect from " + file)
    name = "data/mm10_data/DHS_intersect_" + file + ".csv"
    DHS_data = pd.read_csv(name, header=None, index_col=False)
    init_chromosome = []
    init_start = []
    init_end = []
    init_type = []
    init_other_cells = []

    chromosome = []
    start = []
    end = []
    type = []
    other_cells = []
    repeats = {}
    confluency = {}
    retain = []

    #drop redundant data
    # DHS_data.drop(DHS_data.columns[5], 1, inplace=True)
    # DHS_data.drop(DHS_data.columns[5], 1, inplace=True)
    # DHS_data.drop(DHS_data.columns[5], 1, inplace=True)
    # DHS_data.drop(DHS_data.columns[5], 1, inplace=True)

    #0=chromosome 1=start 2=end 3=type 4=other cell presence
    #use as DHS_data[4]
    #DHS_data[col][row] = value in df
    # for col in DHS_data:
    #     print(str(col))
        # for row in DHS_data[col]:
        #     print(row)
    for row in DHS_data[0]:
        init_chromosome.append(row)
    for row in DHS_data[1]:
        init_start.append(row)
    for row in DHS_data[2]:
        init_end.append(row)
    for row in DHS_data[3]:
        init_type.append(row)
    for row in DHS_data[4]:
        init_other_cells.append(row)

    def duplicates(list, item):
        return [i for i, x in enumerate(list) if x == item]

    ##gut anything that isn't an enchacer or intergenic
    retain = duplicates(init_type, "Intergenic")
    for index in retain:
        chromosome.append(init_chromosome[index])
        start.append(init_start[index])
        end.append(init_end[index])
        type.append(init_type[index])
        other_cells.append(init_other_cells[index])

    unique_starts = set(start)

    for unit in unique_starts:
        repeats[str(unit)] = duplicates(start, unit)

    # print(repeats)

    for place in repeats:
        all_cells = ['1cell','2cell','4cell','8cell']
        cell = []
        blackout = []
        name = str(chromosome[repeats[place][0]]) + ":" + str(place) + "-" + str(end[repeats[place][0]])
        for index in repeats[place]:
            cell.append(other_cells[index])
        cell_name = file + 'cell'
        cell.append(cell_name)
        cell.sort()
        for count in all_cells:
            if count not in cell:
                blackout.append(count)
        for zero in blackout:
            marker = str(zero) + "-"
            cell.append(marker)
        cell.sort()
        for placeholder in cell:
            if "-" in placeholder and "1cell" in placeholder:
                cell[0] = 0
            elif "1cell" in placeholder and "-" not in placeholder:
                cell[0] = 1

            if "-" in placeholder and "2cell" in placeholder:
                cell[1] = 0
            elif "2cell" in placeholder and "-" not in placeholder:
                cell[1] = 1

            if "-" in placeholder and "4cell" in placeholder:
                cell[2] = 0
            elif "4cell" in placeholder and "-" not in placeholder:
                cell[2] = 1

            if "-" in placeholder and "8cell" in placeholder:
                cell[3] = 0
            elif "8cell" in placeholder and "-" not in placeholder:
                cell[3] = 1                           
        confluency[name] = cell
    #TODO:
    #Export to csv
    #print(confluency)
    # print("Length before " + file + " " + str(len(final_data_dict)))
    final_data_dict.update(confluency)
    # print("Length of confluency at " + file + " " + str(len(confluency)))
    # print("Length after " + file + " " + str(len(final_data_dict)))
    # if file == '8':
    #     for data in confluency:
    #         if data in final_data_dict:
    #             print(data)

# for x in range(len(final_data_dict)):
#     line = []
#     line.append(final_data_dict.keys())
#     for key in final_data_dict.keys(): 
#         for x in range(3):
#             line.append(final_data_dict[key][x])
#     final_data_list.append(line)
# print(final_data_list)
for entry in final_data_dict.items():
    final_data_list.append((entry[0], entry[1][0], entry[1][1], entry[1][2], entry[1][3]))
df = pd.DataFrame(final_data_list)
df.to_csv("data/mm10_data/analyzed_intersects.csv", index=False, header=False)
