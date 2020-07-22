path=data/mm10_data/DHSs
#generate new shuffled files
shuf -n 81 $path/DHSs_intergenic_2.bed > $path/shuf_DHSs_2.bed
shuf -n 81 $path/DHSs_intergenic_4.bed > $path/shuf_DHSs_4.bed
shuf -n 81 $path/DHSs_intergenic_8.bed > $path/shuf_DHSs_8.bed
#cat all the shuffled dhs
cat $path/DHSs_intergenic_1.bed > $path/shuf_selection.bed
cat $path/shuf_DHSs_2.bed >> $path/shuf_selection.bed
cat $path/shuf_DHSs_4.bed >> $path/shuf_selection.bed
cat $path/shuf_DHSs_8.bed >> $path/shuf_selection.bed
#construct ids
awk '{print $1":"$2"-"$3}' $path/shuf_selection.bed > $path/shuffled_DHSs.bed


