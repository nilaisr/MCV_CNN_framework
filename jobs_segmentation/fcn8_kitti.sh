#!/bin/bash
#SBATCH -n 4 # Number of cores
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -D /home/grupo07/M5/MCV_CNN_framework # working directory
#SBATCH -t 0-10:05 # Runtime in D-HH:MM
#SBATCH --partition mhigh,mlow
#SBATCH --mem 20000 # 16GB solicitados.
#SBATCH --gres gpu:1 # Para pedir Pascales MAX 8
#SBATCH -o /home/grupo07/logs/segmentation/%x_%u_%j.out # File to which STDOUT will be written
#SBATCH -e /home/grupo07/logs/segmentation/%x_%u_%j.err # File to which STDERR will be written
sleep 5
/usr/local/cuda-9.2/samples/bin/x86_64/linux/release/deviceQuery
nvidia-smi
cd ~/M5/MCV_CNN_framework
python main.py --silent --exp_name fcn8_kitti --exp_folder ~/Experiments/segmentation/ --config_file config/SemSeg_sample_fcn8_KITTI.yml

 
