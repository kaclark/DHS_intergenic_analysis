srun --pty bash
module load bedtools
DHS=data/DHS_data/DHS_intergenic/all_DHSs.bed 
H3K27ac=data/ChIP_data/macs2/H3K27ac_summits.bed 
H3K4me3=data/ChIP_data/H3K4me3/macs2/H3K4me3_summits.bed
Nanog=data/ChIP_data/TF_2/macs2/Nanog_2_summits.bed 
Oct4=data/ChIP_data/TF_2/macs2/Oct4_2_summits.bed 
Sox2=data/ChIP_data/TF_2/macs2/Sox2_2_summits.bed 
outd=data/ChIP_data/DHS_data  
bedtools window -w 2500 -a $DHS -b $H3K27ac > ${outd}/H3K27ac_window.bed  
bedtools window -w 2500 -a $DHS -b $H3K4me3 > ${outd}/H3K4me3_window.bed
bedtools intersect -wa -a $DHS -b $Nanog > $outd/Nanog_intersect.bed
bedtools intersect -wa -a $DHS -b $Oct4 > $outd/Oct4_intersect.bed
bedtools intersect -wa -a $DHS -b $Sox2 > $outd/Sox2_intersect.bed
