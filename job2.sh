#!/bin/bash
#SBATCH --job-name=mijn_test_job
#SBATCH --output=resultaat_%j.txt
#SBATCH --partition=rome
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

module load 2025
module load Python/3.13.1-GCCcore-14.2.0
source venv/bin/activate

echo "rekennode!"
python -c "import torch; print('Torch versie:', torch.__version__)"
