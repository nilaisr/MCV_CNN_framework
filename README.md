# Scene Understanding for Autonomous Vehicles

## GROUP 07


### Members:
- Marc Nuñez Ubach - <marc.nunezu@e-campus.uab.cat>
- Manuel Rey Area - <mreyarea@gmail.com>
- Nilai Sallent Ruiz - <nilai.sallent@e-campus.uab.cat>
- Aitor Sanchez Abellan - <aitor.sanchez.abellan@gmail.com>

### Project summary
This project is divided in three independent parts or stages, Object Recognition, Object Detection and Image Semantic Segmentation. They are not connectedin the sense that all together form a complete system for one sole purpose. Instead, theyare actually three parts obtaining increasingly more complex results towards one sameend, understand an scene on the basis of the objects it is composed of.

### Overleaf article
(http://bit.ly/2CbLbEq)


# Week 4
### Abstract
This week we had to chose an already existing framework to deal with object detection inside the image. Object detection consist in find and classificate multiple objects inside images. The network selected for this task was the YOLOv3 implemented with Darknet. The datasets tested are the COCO that was already in the dataloader and the TT100K and Udacity that we had to adapt. Then in order to emprove the results, a data augmentation were implemented. 
## Code
[YoloV3 Framework](https://github.com/manurare/yolov3.git)

## How to run it
Install requriements.txt

In order to train: 
    
Download dataset of COCO

    sh data/get_coco_dataset.sh

In order to predict:

    python3 test.py --cfg cfg/yolov3.cfg --data-cfg data/coco.data --weights weights/yolov3.weights --dataset_name coco_predict_valid

## Completed tasks

- [x] (a) Train an existing object detection network 
- [x] (b) Read two papers
- [x] (c) Train the networks on a different dataset
    - [x] TsingHua-TenCent 100K 
    - [ ] KITTI
    - [x] Udacity
- [x] (d) Boost the performance of our network
- [x] (e) Write report


## Implementation

- Run the download framework:
	- YOLOv3 with COCO dataset
- Train each network with the following datasets:
	- Camvid
	- Synthia
- Boost the performance of the networks:
	- Data augmentation
	- Number of epochs
	
## Summary of papers

### Region-based Convolutional Network 
[Network summary](docs/RCNN/README.md)

### You Only Look Once Network 
[Network summary](docs/YOLO/README.md)

### Google Slides
[Sides](https://docs.google.com/presentation/d/1y6tMXZfgE9osZ900mdlckLrv19ThAQ9OXcoHZ7ij84g/edit?usp=sharing)


### Model weights
- [COCO](https://drive.google.com/file/d/19pDrYT1UXjYzAkKNBkHyfI2zNcXCp3A0/view?usp=sharing)
- [TT100K](https://drive.google.com/file/d/19Mg59nrzz2VkPAuJqxFcMHMoDz_P9_AC/view?usp=sharing)
- [Udacity](https://drive.google.com/file/d/1K7wHensMr1inzUDvCKdZr8CJQEPCqSdW/view?usp=sharing)

# Week 3
### Abstract
During this week we have focused on the task of semantic segmentation in images. Semantic Segmentation consist on detecting the exact pixel areas different objects -belonging to the same class- occupy in the image. We have train different networks (fcn8, deeplabv3plus) in different datasets (Camvid, KITTI and Synthia) in order to test their performance. We also applied data augmentation over the dataset images. Two papers about semantic segmentation needed to be chosen and read as well.

## Completed tasks

- [x] (a) Run the provided code
- [x] (b) Read two papers
- [x] (c) Implement a new Network
    - [x] Using an existing PyTorch implementation.
- [x] (d) Train the network on a different datasets
- [x] (e) Boost the performance of our network
- [x]  (f) Write report

## Summary of papers

### FC Semantic Segmentation
[Network summary](docs/FC-Semantic/README.md)

### DeepLabV3+
[Network summary](docs/deeplab/README.md)

### Google Slides
[Slides](https://bit.ly/2usnfIQ)

### Model weights
- [DeeplabV3Plus KITTI](https://drive.google.com/open?id=1bHkuiKvj0OEsFIITTP-vT8HU2bl9qGM_)
- [FCN8 KITTI](https://drive.google.com/open?id=1JGMv4aGmpFHdrWICZIra_rp64a_WeQ53)

## Implementation

- Run the provided code:
	- Fcn8 with Camvid dataset.
- Implement Networks:
    - Using an existing PyTorch implementation:
		- DeepLabv3_plus
- Train each network with the following datasets:
	- Camvid
	- KITTI 
	- Synthia
- Boost the performance of the networks:
	- Data augmentation
	- Number of epochs

## How to run it
`python main.py --silent --exp_name net_dataset  --exp_folder ~/Experiments/segmentation/ --config_file config/SemSeg_sample_net_dataset.yml`

Specifying the configuration file wanted and an experiment name for the results folder.

# Week 2

## Summary of papers

### VGG
[Network summary](docs/VGG/README.md)


### Inception-ResNet
[Network summary](docs/Inception-ResNet/README.md)

### Google Slides
(http://bit.ly/2Hd15m0)

### Google Drive, Weights of the models
(https://drive.google.com/open?id=1AyNBKUyOUVAb3ow-_CWKRhQtB5kVna1e)

## Completed tasks

- [x] (a) Run the provided code & transfer learning
- [x] (b) Train a network on another dataset
- [x] (c) Implement a new Network
- [x] (e) Report showing the achieved results

## Implementation

- Run the provided code:
	- VGG16 with TT100K dataset.
	- Transfer learning to KITTI dataset.
- Implement NEW Network:
	- SqueezeNet


## How to run it
`python3 main.py --config_file config/configFile.yml --exp_name experiment`

Specifying the configuration file wanted and an experiment name for the results folder.


## Results
### Acc

| Datasets | Networks  | train  | val   | test  |
|----------|-----------|--------|-------|-------|
| TT100k   | VGG-16    | 96.19%      | 96.19%     | 96.50%     |
|          | VGG-16 <br> Preprocessing   | 96.19%      | 96.51%     | 96.21%     |
|          | SqueezeNet | 95.68%      | 95.66%     | 95.66%     |
|	   | SqueezeNet <br> Preprocessing | 95.90%      | 95.81%     | 95.91%     |
| KITTI    | VGG-16    | 98.55%      | 98.10%     | 98.25%     |
|          | VGG-16 <br> Preprocessing   | 99.01%      | 98.52%     | 98.48%     |

### Loss

| Datasets | Networks  | train  | val   | test  |
|----------|-----------|--------|-------|-------|
| TT100k   | VGG-16    | 3.4837      | 3.4837     | 0.0815     |
|          | VGG-16 <br> Preprocessing   | 3.4822     | 0.0814     | 0.0731     |
|          | SqueezeNet | 3.8286      | 0.0983     | 0.0983     |
|          | SqueezeNet <br> Preprocessing | 3.8286      | 0.0983     | 0.0962     |
| KITTI    | VGG-16    | 3.654      | 0.0876     | 0.0876     |
|          | VGG-16 <br> Preprocessing | 3.746      | 0.0934     | 0.0934     |
