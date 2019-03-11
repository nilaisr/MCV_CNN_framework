### VGG summary 
__*Simonyan, Karen, and Andrew Zisserman. "Very deep convolutional networks for large-scale image recognition." arXiv preprint arXiv:1409.1556 (2014).*__

The ConvNets presented in this paper is more accurate than previous ones that achieve state-of-the-art accuracy on ILSVRC, and are also applicable to other image recognition datasets.

As an improvement, they only use stack of convolutional filters of size 3x3 and 1x1. The stack of several of the former layers allows the same effectiveness of larger filters with reduced number of parameters. The latter configuration is used to apply a linear transformation that reduces the non-linearity of the decision function without affecting the receptive fields of the convolutional layers. The stride was set to 1 so that preserved the spatial resolution. Spatial pooling is carried out by a max-pooling layer after some of the convolutions with a 2x2 window and stride 2.

All hidden layers are equiped with the rectification (ReLU) non-linearity and the Local Response Normalization is not used sice leads to increased memory consumption and computational time without improving the results.

Smaller convolutional filters had been used previously, but with narrower nets and they were evaluated with other datasets. It had been shown previously that increasing the depth of the network lead to a better performance. GoogLeNet also used smaller filters but with a more complex network topology and applaying a more aggressive reduction of the feature maps to the first layers to reduce computational cost.

Although the network proposed has a large number of parameters it requires less epochs to converge given the implicit regularization and the pre-initialization of certain layers.

The model generalizes well with a wide range of datasets and tasks, matching or outperforming other recognition pipelines of more complexity build arround less deep image representations. This confirms the relevance of depth in visual representations.
