library(EnrichedHeatmap)
library(rtracklayer)
library(GenomicRanges)

DHSs.bed <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/DHSs/all_DHSs.bed", format="BED")

H3K27ac.bw <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/ChIP_visual/H3K27ac.bw", format="BigWig")

DHSs.10kb <- resize(DHSs.bed, width=1, fix="center")
DHSs.10kb.center <- resize(DHSs.10kb, width=1, fix="center")

H3K27ac.mat <- normalizeToMatrix(H3K27ac.bw, DHSs.10kb.center, value_column="score", mean_mode="w0", w=100, extend=2500)

quantile(H3K27ac.mat, probs = c(0.005, 0.5, 0.90))

library(circlize)

col_fun_H3K27ac <- circlize::colorRamp2(c(0, 100), c("white", "blue"))

EnrichedHeatmap(H3K27ac.mat, axis_name_rot = 0, name = "H3K27ac", column_title = "H3K27ac - All Intergenic DHSs", use_raster = TRUE, col = col_fun_H3K27ac, top_annotation = HeatmapAnnotation(lines = anno_enriched()))

