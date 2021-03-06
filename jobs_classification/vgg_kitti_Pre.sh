#!/bin/bash
#SBATCH -n 4 # Number of cores
#SBATCH --mem 20000 # 2GB solicitados.
#SBATCH -D /home/grupo07/M5/MCV_CNN_framework # working directory
#SBATCH -p mhigh,mlow# or mlow Partition to submit to
#SBATCH --gres gpu:1 # Para pedir Pascales MAX 8
#SBATCH -o ../../logs/%x_%u_%j.out # File to which STDOUT will be written
#SBATCH -e ../../logs/%x_%u_%j.err # File to which STDERR will be written
#SBATCH --job-name vgg_kitti_Pre

python3 main.py --config_file config/vgg_kittiPre.yml --exp_name vgg_kitti_Pre

