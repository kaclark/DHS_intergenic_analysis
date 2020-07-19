#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=ChIP_TFs

module load perl/5.24.1 sra/2.10.0
module load bwa samtools
module load bedtools ucsc-tools
module load python deeptools

cd ~/data/ChIP_data/

mkdir TF_2
cd TF_2

mkdir fastq
mkdir bam
mkdir bigwig
mkdir visualize

# add SRR ids to text file
echo SRR713342 >> SRR_ids.txt
echo SRR713342 >> Samples.txt
echo SRR713340 >> SRR_ids.txt
echo SRR713340 >> Samples.txt
echo SRR713341 >> SRR_ids.txt
echo SRR713341 >> Samples.txt
echo SRR713343 >> SRR_ids.txt


cd bigwig
mkdir bam
cd ..

CONTROL=SRR713343
REF=~/data/ChIP_data/reference/mm10.fa  

# download fasta files of H3K4me3 and control
cat SRR_ids.txt | parallel "fastq-dump --outdir fastq --split-files -F {}"

# Align fastq to genome
cat SRR_ids.txt | parallel "bwa mem -t 4 $REF fastq/{}_1.fastq | samtools sort > bam/{}.bam"

# generate bedgraph and bigwig
ls bam/*.bam | parallel "bedtools genomecov -ibam {} -g $REF.fai -bg | sort -k1,1 -k2,2n > {.}.bedgraph"
ls bam/*.bedgraph | parallel --eta --verbose "bedGraphToBigWig {} $REF.fai bigwig/{.}.bw"

# remove bigwig from bam folder in bigwig directory
cd ~/data/ChIP_data/TF_2/bigwig/bam
mv *.bw ~/data/ChIP_data/TF_2/bigwig

# obtain peaks
cd ~/data/ChIP_data/TF_2/
mkdir macs2
cat Samples.txt | parallel "macs2 callpeak -t bam/{}.bam -c bam/${CONTROL}.bam -n {} --outdir macs2"

# visualization
cat Samples.txt | parallel "bigwigCompare --bigwig1 bigwig/{}.bw --bigwig2 bigwig/${CONTROL}.bw --operation subtract -o bigwig/{}_minus_ctrl.bw"

DHS=~/data/DHS_data/DHS_intergenic/all_DHSs.bed
cat Samples.txt | parallel "computeMatrix scale-regions -R $DHS -S bigwig/{}_minus_ctrl.bw -o visualize/{}.gz"

cat Samples.txt | parallel "plotHeatmap -m visualize/{}.gz -o visualize/{}.png --colorList 'white,blue'"

# cd ~/data/mm10_data/intersect_groups/

# cat Samples.txt | parallel "computeMatrix scale-regions -R {}.bed - S ~/data/ChIP_data/TF/bigwig/{}_minus_ctrl.bw -o ~/data/ChIP_data/TF/visualize/{}.gz"

# cd ~/data/ChIP_data/TF/visualize

# ls *.gz | parallel "plotHeatmap -m {} -o {}.png --colorList 'white,blue'"





