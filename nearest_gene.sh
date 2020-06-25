#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=nearest_gene

module load python3
python3 nearest_gene.py