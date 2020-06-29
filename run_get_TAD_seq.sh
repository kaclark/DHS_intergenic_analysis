#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=END
#SBATCH --mail-user=kaclark@mit.edu
#SBATCH --job-name=get_TAD_seq

module load python3
python3 get_TAD_seq.py