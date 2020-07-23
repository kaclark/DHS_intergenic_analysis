module load bedtools
bedtools sort -i data/SE/super_enhancers.bed > data/SE/sorted_SE.bed
SE=data/SE/sorted_SE.bed
DHS1=data/mm10_data/DHSs/DHSs_sorted_1.bed
DHS2=data/mm10_data/DHSs/DHSs_sorted_2.bed
DHS4=data/mm10_data/DHSs/DHSs_sorted_4.bed
DHS8=data/mm10_data/DHSs/DHSs_sorted_8.bed
outf=data/SE/SE_intersects.bed
bedtools intersect -wa -wb -a $SE -b $DHS1 $DHS2 $DHS4 $DHS8 > $outf
cd data/SE
awk '{print $1":"$2"-"$3, $5":"$6"-"$7}' SE_intersects.bed > SE_intersects_w_repeats.bed
awk '!seen[$0]{print}{++seen[$0]}' SE_intersects_w_repeats.bed  > uq_SE_intersects.bed
tr ' ' ',' < uq_SE_intersects.bed > SE_intersects.csv
