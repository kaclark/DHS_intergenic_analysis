#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=ChIP_H3K4me3

module load perl/5.24.1 sra/2.10.0
module load bwa samtools
module load bedtools ucsc-tools
module load python deeptools

cd ~/data/ChIP_data/H3K4me3

SAMPLE=SRR066769
CONTROL=SRR066787  

# visualization
bigwigCompare --bigwig1 bigwig/${SAMPLE}.bw --bigwig2 bigwig/${CONTROL}.bw --operation subtract -o bigwig/${SAMPLE}_minus_ctrl.bw

DHS=~/data/DHS_data/DHS_intergenic/all_DHSs.bed
computeMatrix scale-regions -R $DHS -S bigwig/${SAMPLE}_minus_ctrl.bw -o visulaize/${SAMPLE}.gz

plotHeatmap -m visualize/${SAMPLE}.gz -o visualize/${SAMPLE}.png --colorList 'white,blue'

cd ~/data/mm10_data/intersect_groups/

ls *.bed | parallel "computeMatrix scale-regions -R {} - S ~/data/ChIP_data/H3K4me3/bigwig/${SAMPLE}_minus_ctrl.bw -o ~/data/ChIP_data/H3K4me3/visualize/{}.gz"

cd ~/data/ChIP_data/H3K4me3/visualize

ls *.gz | parallel "plotHeatmap -m {} -o {}.png --colorList 'white,blue'"





