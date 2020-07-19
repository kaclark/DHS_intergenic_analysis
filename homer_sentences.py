import sys
from pathlib import Path
import pandas as pd

directory = sys.argv[1]
pathlist = Path(directory).glob('*.motif')
export_data = []
printed = False
for motif in pathlist:
    result = str(motif).split('\\')[-1]
    number_with_motif_extension = result.split('n')[-1]
    rank = int(number_with_motif_extension.split('.')[0])
    if rank < 25:
        with open(motif) as data:
            first_line = True
            for line in data:
                if first_line == True:
                    raw_line = str(line)
                    line_list = raw_line.split('\t')
                    pre_seq = line_list[0]
                    pre_tf_name = line_list[1]
                    seq = pre_seq[1:]
                    tf_name = pre_tf_name.split('/')[0]
                    export_data.append('>' + tf_name)
                    export_data.append(seq)
                    first_line = False

motif_df = pd.DataFrame(export_data)
motif_df.to_csv('data/mm10_data/homer/homer_sentences.fa', index=False, header=False)
print("Homer sentences exported!")
