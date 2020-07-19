#!/bin/bash

module load perl/5.24.1 sra/2.10.0
module load bwa samtools
module load bedtools ucsc-tools
module load python deeptools

cd ~/data/ChIP_data/
mkdir fastq
mkdir bam
mkdir reference
mkdir bigwig
mkdir visualize

# get the fastq files
cat SRR_ids.txt | parallel "fastq-dump --outdir fastq --split-files -F {}"

# download fasta files of reference genome
REF=reference/mm10.fa
URL=http://hgdownload.cse.ucsc.edu/goldenPath/mm10/bigZips/chromFa.tar.gz
curl $URL | tar zxv
mv *.fa reference
cat refs/chr*.fa > $REF

# index my reference genome
bwa index $REF
samtools index $REF

# align fastq to genome
cat SRR_ids.txt | parallel "bwa mem -t 4 $REF fastq/{}_1.fastq | samtools sort > bam/{}.bam"

# visualize alignments by creating bedgraph and bigwig file
# this will put the try to save the files to bigwig/bam/filename.bw but the
# bam dir will not exist so it will give an error
# addition of this dir will solve this issue
ls bam/*.bam | parallel "bedtools genomecov -ibam {} -g $REF.fai -bg | sort -k1,1 -k2,2n > {.}.bedgraph"
ls bam/*.bedgraph | parallel --eta --verbose "bedGraphToBigWig {} $REF.fai bigwig/{.}.bw"
# bam needs to be made once and then left
cd ~/data/ChIP_data/bigwig/bam
mv *bw ~/data/ChIP_data/bigwig
cd ..head


# subtract control signal from sample
# remove the bw files from the bam dir into the bigwig dir above it
CONTROL=SRR066787 #SRR ID for the control
SAMPLE=SRR066766 #SRR ID for the sample
bigwigCompare --bigwig1 bigwig/${SAMPLE}.bw --bigwig2 bigwig/${CONTROL}.bw --operation subtract -o bigwig/${SAMPLE}_minus_ctrl.bw

# make directory for wig and bed files
mkdir wig
mkdir bed
# load bedops
module load bedops/2.4.35 python3/3.6.4
#convert bigwig to wig
bigWigToWig bigWig/${SAMPLE}_minus_ctrl.bw wig/${SAMPLE}_minus_ctrl.wig
#convert wig to bed
wig2bed < wig/${SAMPLE}_minus_ctrl.wig > bed/${SAMPLE}_minus_ctrl.bed
#That did not give me what I wanted

#Call peaks
moudle load macs2
cd ~/data/ChIP_data/
mkdir macs2
macs2 -t bam/${SAMPLE}.bam -c bam/${CONTROL}.bam -outdir macs2

# see signal at my regions of interest
DHS=~data/DHS_data/DHS_intergenic/all_DHSs.bed
computeMatrix scale-regions -R $DHS -S bigwig/${SAMPLE}_minus_ctrl.bw -o visualize/${SAMPLE}.gz
plotHeatmap -m visualize/${SAMPLE}.gz -o visualize/${SAMPLE}.png --colorList 'white,blue'

cd ~/data/mm10_data/intersect_groups/

ls *.bed | parallel "computeMatrix scale-regions -R {} -S ~/data/ChIP_data/bigwig/${SAMPLE}_minus_ctrl.bw -o ~/data/ChIP_data/visualize/{}.gz"

cd ~/data/ChIP_data/visualize

ls *.gz | parallel "plotHeatmap -m {} -o {}.png --colorList 'white,blue'"
