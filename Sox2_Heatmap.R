library(EnrichedHeatmap)
library(rtracklayer)
library(GenomicRanges)

DHSs.bed <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/DHSs/all_DHSs.bed", format="BED")

Sox2.bw <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/ChIP_visual/Sox2.bw", format="BigWig")

DHSs.10kb <- resize(DHSs.bed, width=1, fix="center")
DHSs.10kb.center <- resize(DHSs.10kb, width=1, fix="center")

Sox2.mat <- normalizeToMatrix(Sox2.bw, DHSs.10kb.center, value_column="score", mean_mode="w0", w=100, extend=2500)

quantile(Sox2.mat, probs = c(0.005, 0.5, 0.90))

library(circlize)

col_fun_Sox2 <- circlize::colorRamp2(c(0, 100), c("white", "blue"))

EnrichedHeatmap(Sox2.mat, axis_name_rot = 0, name = "Sox2", column_title = "Sox2 - All Intergenic DHSs", use_raster = TRUE, col = col_fun_Sox2, top_annotation = HeatmapAnnotation(lines = anno_enriched()))

