library(EnrichedHeatmap)
library(rtracklayer)
library(GenomicRanges)

DHSs.bed <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/DHSs/all_DHSs.bed", format="BED")

Nanog.bw <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/ChIP_visual/Nanog_2.bw", format="BigWig")

DHSs.10kb <- resize(DHSs.bed, width=1, fix="center")
DHSs.10kb.center <- resize(DHSs.10kb, width=1, fix="center")

Nanog.mat <- normalizeToMatrix(Nanog.bw, DHSs.10kb.center, value_column="score", mean_mode="w0", w=100, extend=500)

quantile(Nanog.mat, probs = c(0.005, 0.5, 0.90))

library(circlize)

col_fun_Nanog <- circlize::colorRamp2(c(0, 100), c("white", "blue"))

EnrichedHeatmap(Nanog.mat, axis_name_rot = 0, name = "Nanog", column_title = "Nanog - All Intergenic DHSs", use_raster = TRUE, col = col_fun_Nanog, top_annotation = HeatmapAnnotation(lines = anno_enriched()))


