library(ggpubr)
#length_1_2_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/1_2_4_8_length.csv", header=FALSE)
#length_1_2_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/1_2_8_length.csv", header=FALSE)
#length_1_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/1_4_8_length.csv", header=FALSE)
#length_1_4 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/1_4_length.csv", header=FALSE)
#length_1_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/1_8_length.csv", header=FALSE)
#length_1 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/1_length.csv", header=FALSE)
#length_2_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/2_4_8_length.csv", header=FALSE)
#length_2_4 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/2_4_length.csv", header=FALSE)
#length_2_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/2_8_length.csv", header=FALSE)
#length_2 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/2_length.csv", header=FALSE)
#length_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/4_8_length.csv", header=FALSE)
#length_4 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/4_length.csv", header=FALSE)
#length_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/8_length.csv", header=FALSE)

#length_data = c(length_1_2_4_8, length_1_2_8, length_1_4_8, length_1_4, length_1_8, length_1, length_2_4_8, length_2_4, length_2_8, length_2, length_4_8, length_4, length_8)
#gc_1_2_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/1_2_4_8_gc.csv", header=FALSE)
##gc_1_2_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/1_2_8_gc.csv", header=FALSE)
#gc_1_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/1_4_8_gc.csv", header=FALSE)
#gc_1_4 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/1_4_gc.csv", header=FALSE)
#gc_1_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/1_8_gc.csv", header=FALSE)
#gc_1 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/1_gc.csv", header=FALSE)
#gc_2_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/2_4_8_gc.csv", header=FALSE)
#gc_2_4 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/2_4_gc.csv", header=FALSE)
#gc_2_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/2_8_gc.csv", header=FALSE)
#gc_2 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/2_gc.csv", header=FALSE)
#gc_4_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/4_8_gc.csv", header=FALSE)
#gc_4 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/4_gc.csv", header=FALSE)
#gc_8 <- read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/8_gc.csv", header=FALSE)

gc_data = c(gc_1_2_4_8, gc_1_2_8, gc_1_4_8, gc_1_4, gc_1_8, gc_1, gc_2_4_8, gc_2_4, gc_2_8, gc_2, gc_4_8, gc_4, gc_8)
par(mar=c(4.5,4.5,4.5,4.5))
length_data = read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/length/all_lengths.csv") 
head(length_data)
par(cex.lab=0.65) # is for y-axis
par(cex.axis=0.65) # is for x-axis
ggboxplot(length_data, x="Group", y="Length", title="Length Venn Partition", fill="blue", notch=TRUE)+
  stat_compare_means(method = "kruskal.test")
gc_data = read.csv("C:/Users/da1an/Documents/UROP/luria/DHS_intergenic_analysis/data/mm10_data/intersects/venn_partitions/proc_data/gc/all_gc.csv") 
ggboxplot(gc_data, x="Group", y="GC", title="GC Venn Partition", fill="blue", notch=TRUE)+
  stat_compare_means(method = "kruskal.test")
#boxplot(
#  length_data,
#  main = "Length Venn Partitions",
#  notch=TRUE,
#  xlab = "Venn Group",
#  ylab = "Sequence Length",
#  show.names = TRUE,
#  names = c("1:2:4:8", "1:2:8", "1:4:8", "1:4", "1:8", "1", "2:4:8", "2:4", "2:8", "2", "4:8","4", "8")
#)
