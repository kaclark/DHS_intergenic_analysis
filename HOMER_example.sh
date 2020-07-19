#!/bin/bash

module load bedtools python homer

# mm10=~/data/genome/mm10/mm10.fa
mm10=~/data/genomes/mm10.fa
mm10chr=~/data/genomes/mm10.chrom.sizes
# mm10chr=~/data/genome/mm10.chrom.sizes
#wget https://hgdownload.soe.ucsc.edu/goldenPath/mm10/bigZips/mm10.chrom.sizes

##### get sequence of your regions of interest
# every sequence needs to have a unique identifier for HOMER to work
# you can also use homerTools extract to do this
# make compiled file with all unique DHSs from all cell counts 
# query_bed=~/data/homer/my_sites_of_interest.bed
query_bed=~/data/DHS_data/DHS_intergenic/all_DHSs.bed
query_seq=~/data/DHS_data/fa/all_DHSs.fa

# query_seq=~/data/homer/my_sites_of_interest.fasta
bedtools getfasta -fi $mm10 -bed $query_bed -fo $query_seq

##### get sequence of your background
# three main options (run one of these):
# 1. if you have an actual background list, use that
bckgd_bed=~/data/homer/my_background.bed
bckgd_seq=~/data/homer/my_background.fasta
bedtools getfasta -fi $mm10 -bed $query_bed -fo $bckgd_seq

# 2. scramble your input sequence
bckgd_seq=~/data/homer/my_sites_of_interest_scramble.fasta
scrambleFasta.pl $query_seq > $bckdg_seq

#3. get random regions from the genome of the same size as your sequence
bckgd_bed=~/data/homer/all_DHSs_shuffle.bed
bckgd_seq=~/data/homer/all_DHSs_shuffle.fasta
#TODO: finish this 
bedtools shuffle -i data/DHS_data/DHS_intergenic/all_DHSs.bed -excl data/DHS_data/DHS_intergenic/all_DHSs.bed -g data/genomes/mm10.chrom.sizes > data/DHS_data/DHS_intergenic/all_DHSs_shuffled.bed
bedtools getfasta -fi data/genomes/mm10.fa -bed data/DHS_data/DHS_intergenic/all_DHSs_shuffled.bed > data/DHS_data/fa/all_DHSs_shuffled.fa


##### run homer
# run homer
findMotifs.pl data/DHS_data/fa/all_DHSs.fa fasta data/homer -fasta data/DHS_data/fa/all_DHSs_shuffled.fa
