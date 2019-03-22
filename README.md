# Scene Understanding for Autonomous Vehicles

## GROUP 07


### Members:
- Marc Nuñez Ubach - <marc.nunezu@e-campus.uab.cat>
- Manuel Rey Area - <mreyarea@gmail.com>
- Nilai Sallent Ruiz - <nilai.sallent@e-campus.uab.cat>
- Aitor Sanchez Abellan - <aitor.sanchez.abellan@gmail.com>

### Project summary
This project is divided in three independent parts or stages, Object Recognition, Object Detection and Image Semantic Segmentation. They are not connectedin the sense that all together form a complete system for one sole purpose. Instead, theyare actually three parts obtaining increasingly more complex results towards one sameend, understand an scene on the basis of the objects it is composed of.

## Week 3
### Abstract
During this week we have focused on the task of semantic segmentation in images. Semantic Segmentation consist on detecting the exact pixel areas different objects occupy in the image. We have train different networks (fcn8) in different datasets (Camvid, KITTI...) in order to test their performance. We also applied data augmentation over the dataset images. Two papers about semantic segmentation needed to be chosen and read as well.

## Completed tasks

- [x] (a) Run the provided code
- [x] (b) Read two papers
- [x] (c) Implement a new Network
    - [x] Using an existing PyTorch implementation.
- [x] (d) Train the network on a different datasets
- [x] (e) Boost the performance of our network
- []  (f) Write report

## Implementation

- Run the provided code:
	- Fcn8 with Camvid dataset.
- Implement Networks:
    - Using an existing PyTorch implementation:
		- DeepLabv3_xception
- Train each network with the following datasets:
	- Camvid
	- KITTI 
- Boost the performance of the networks:
	- Data augmentation

## Week 2

### VGG
[Network summary](docs/VGG/README.md)


### Inception-ResNet
[Network summary](docs/Inception-ResNet/README.md)



### Overleaf article
(http://bit.ly/2CbLbEq)

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
