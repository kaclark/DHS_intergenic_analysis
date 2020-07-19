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

cd ~/data/ChIP_data/

mkdir H3K4me3
cd H3K4me3

mkdir fastq
mkdir bam
mkdir bigwig
mkdir visualize

cd bigwig
mkdir bam
cd ..

SAMPLE=SRR066769
CONTROL=SRR066787
REF=~/data/ChIP_data/reference/mm10.fa  

# download fasta files of H3K4me3 and control
fastq-dump --outdir fastq --split-files -F $SAMPLE
fastq-dump --outdir fastq --split-files -F $CONTROL

# Align fastq to genome
bwa mem -t 4 $REF fastq/${SAMPLE}_1.fastq | samtools sort > bam/${SAMPLE}.bam
bwa mem -t 4 $REF fastq/${CONTROL}_1.fastq | samtools sort > bam/${CONTROL}.bam

# generate bedgraph and bigwig
ls bam/*.bam | parallel "bedtools genomecv -ibam {} -g $REF.fai -bg | sort -k1,1 -k2,2n > {.}.bedgraph"
ls bam/*.bedgraph | parallel --eta --verbose "bedGraphToBigWig {} $REF.fai bigwig/{.}.bw"

# remove bigwig from bam folder in bigwig directory
cd ~/data/ChIP_data/H3K4me3/bigwig/bam
mv *.bw ~/data/ChIP_data/H3K4me3/bigwig

# obtain peaks
cd ~/data/ChIP_data/H3K4me3/
mkdir macs2
macs2 callpeak -t bam/${SAMPLE}.bam -c bam/${CONTROL}.bam -n H3K4me3 --outdir macs2

# visualization
bigwigCompare --bigwig1 bigwig/${SAMPLE}.bw --bigwig2 bigwig/${CONTROL}.bw --operation subtract -o bigwig/${SAMPLE}_minus_ctrl.bw

DHS=~/data/DHS_data/DHS_intergenic/all_DHSs.bed
computeMatrix scale-regions -R $DHS -S bigwig/${SAMPLE}_minus_ctrl.bw -o visualize/${SAMPLE}.gz

plotHeatmap -m visualize/${SAMPLE}.gz -o visualize/${SAMPLE}.png --colorList 'white,blue'

cd ~/data/mm10_data/intersect_groups/

ls *.bed | parallel "computeMatrix scale-regions -R {} - S ~/data/ChIP_data/H3K4me3/bigwig/${SAMPLE}_minus_ctrl.bw -o ~/data/ChIP_data/H3K4me3/visualize/{}.gz"

cd ~/data/ChIP_data/H3K4me3/visualize

ls *.gz | parallel "plotHeatmap -m {} -o {}.png --colorList 'white,blue'"





