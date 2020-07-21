import pandas as pd

all_DHSs = pd.read_csv("./data/mm10_data/DHSs/all_DHSs.bed", sep='\t', header=None, index_col=False)

chro = []
start = []
end = []

for row in all_DHSs[0]:
    chro.append(row)
for row in all_DHSs[1]:
    start.append(row)
for row in all_DHSs[2]:
    end.append(row)

ids = []
# new starts and ends for standard window with DHS
nstart = []
nend = []
# window data to be exported
export_data = []
tracking_data = []

# iterate through each DHS site
for x in range(len(chro)):
    dhs_id = str(chro[x]) + ":" + str(start[x]) + "-" + str(end[x])
    ids.append(dhs_id)
    diff = end[x] - start[x]
    # if the difference is odd then add one to the end and recalculate difference
    # odd DHSs will be shifted down one in the array
    if diff % 2 != 0:
        end[x] += 1
        diff = end[x] - start[x]
    # calculate extension number for dhs
    standard_window = 1000
    ext = (standard_window - diff) / 2
    new_start = int(start[x] - ext)
    new_end = int(end[x] + ext)
    export_data.append([chro[x], new_start, new_end])
    window_id = str(chro[x] + ":" + str(new_start) + "-" + str(new_end))
    tracking_data.append([dhs_id, window_id])

export_dataframe = pd.DataFrame(export_data)
export_dataframe.to_csv("./data/mm10_data/DHSs/extended_DHSs.bed", sep='\t', index=False, header=False)

tracking_dataframe = pd.DataFrame(tracking_data)
tracking_dataframe.to_csv("./data/mm10_data/DHSs/extended_DHSs_tracking.bed", sep='\t', index=False, header=False)




