srun --pty bash
module load bedtools
DHS=data/DHS_data/DHS_intergenic/extended_DHSs.bed  
mm10=data/genomes/mm10.fa 
outf=data/DHS_data/fa/extended_DHSs.fa 
bedtools getfasta -fi $mm10 -bed $DHS > $outf 
