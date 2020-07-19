library(EnrichedHeatmap)
library(rtracklayer)
library(GenomicRanges)

DHSs.bed <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/DHSs/all_DHSs.bed", format="BED")

Oct4.bw <- import("C:/Users/12283/Documents/Github/DHS_intergenic_analysis/data/mm10_data/ChIP_visual/Oct4.bw", format="BigWig")

DHSs.10kb <- resize(DHSs.bed, width=1, fix="center")
DHSs.10kb.center <- resize(DHSs.10kb, width=1, fix="center")

Oct4.mat <- normalizeToMatrix(Oct4.bw, DHSs.10kb.center, value_column="score", mean_mode="w0", w=100, extend=2500)

quantile(Oct4.mat, probs = c(0.005, 0.5, 0.90))

library(circlize)

col_fun_Oct4 <- circlize::colorRamp2(c(0, 100), c("white", "blue"))

EnrichedHeatmap(Oct4.mat, axis_name_rot = 0, name = "Oct4", column_title = "Oct4 - All Intergenic DHSs", use_raster = TRUE, col = col_fun_Oct4, top_annotation = HeatmapAnnotation(lines = anno_enriched()))

