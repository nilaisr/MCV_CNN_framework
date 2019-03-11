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

### Google Slides
(http://bit.ly/2Hd15m0)

### Google Drive, Weights of the models
(TODO)

## Completed tasks

- [x] (a) Run the provided code & transfer learning
- [x] (b) Train a network on another dataset
- [x] (c) Implement a new Network
- [x] (e) Report showing the achieved results

## Implementation

- Run the provided code:
	- VGG16 with TT100K dataset.
	- Transfer learning to KITTI dataset.
- Implement NEw Network:
	- SqueezeNet

## Results
### Acc

| Datasets | Networks  | train  | val   | test  |
|----------|-----------|--------|-------|-------|
| TT100k   | VGG-16    | -      | -     | -     |
|          | SqueezeNe | -      | -     | -     |
| KITTI    | VGG-16    | -      | -     | -     |
|          | SqueezeNe | -      | -     | -     |

### Loss

| Datasets | Networks  | train  | val   | test  |
|----------|-----------|--------|-------|-------|
| TT100k   | VGG-16    | -      | -     | -     |
|          | SqueezeNe | -      | -     | -     |
| KITTI    | VGG-16    | -      | -     | -     |
|          | SqueezeNe | -      | -     | -     |



## How to run it
`python3 main.py --config_file config/configFile.yml --exp_name experiment`
Specifying the configuration file wanted and an experiment name for the results folder.

## Papers Research
### VGG summary 
__*Simonyan, Karen, and Andrew Zisserman. "Very deep convolutional networks for large-scale image recognition." arXiv preprint arXiv:1409.1556 (2014).*__

The ConvNets presented in this paper is more accurate than previous ones that achieve state-of-the-art accuracy on ILSVRC, and are also applicable to other image recognition datasets.

As an improvement, they only use stack of convolutional filters of size 3x3 and 1x1. The stack of several of the former layers allows the same effectiveness of larger filters with reduced number of parameters. The latter configuration is used to apply a linear transformation that reduces the non-linearity of the decision function without affecting the receptive fields of the convolutional layers. The stride was set to 1 so that preserved the spatial resolution. Spatial pooling is carried out by a max-pooling layer after some of the convolutions with a 2x2 window and stride 2.

All hidden layers are equiped with the rectification (ReLU) non-linearity and the Local Response Normalization is not used sice leads to increased memory consumption and computational time without improving the results.

Smaller convolutional filters had been used previously, but with narrower nets and they were evaluated with other datasets. It had been shown previously that increasing the depth of the network lead to a better performance. GoogLeNet also used smaller filters but with a more complex network topology and applaying a more aggressive reduction of the feature maps to the first layers to reduce computational cost.

Although the network proposed has a large number of parameters it requires less epochs to converge given the implicit regularization and the pre-initialization of certain layers.

The model generalizes well with a wide range of datasets and tasks, matching or outperforming other recognition pipelines of more complexity build arround less deep image representations. This confirms the relevance of depth in visual representations.


### Inception-v4 summary

__*Szegedy, Christian, et al. "Inception-v4, inception-resnet and the impact of residual connections on learning." Thirty-First AAAI Conference on Artificial Intelligence. 2017.*__
 
Google Inc presents their latest revisions of the Inception architecture (Beginning with Inception-v4 and forward). These models are compared and combined with ResNet approaches to quantify the effect of residual connections and their benefits on very deep neural network classification models.
 
First, comparing Inception-v4 with previous inception models, it implements a more uniform simplified architecture and a greater number of inception modules.  This was achieved partly because the migration to a TensorFlow framework which allowed for a simpler deployment of the training model. 
 
Second, ResNet authors argued that residual connections are inherently necessary for training very deep convolutional models. Google experiments demonstrate that it is not very difficult to train very deep competitive models without using them. However residual connections seem to improve the training speed greatly. 
 
Finally, Google combines both architectures, they are named Inception-Resnet models. It was found that models following this architecture exceeding 1000 filters behaves unstably in training even with very low learning rate values. It could be mitigating by scaling down the residuals before adding them to the previous layer. 
 
As a result, google concludes that their two new models, Inception-v4 and Incpetion-ResNet-v2 obtained roughly the same recognition performance and outperformed previous models. Moreover, the use of residual connections leads to dramatically improved training speed for the Inception architecture. 
