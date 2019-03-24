### Fully Convolutional Networks for Semantic Segmentation 
__*Jonathan Long, Evan Shelhamer, and Trevor Darrell. "Fully Convolutional Networks for Semantic Segmentation ." arXiv preprint arXiv:1409.1556 (2014).*__

This paper presents how convolutional networks  can be used for semantic segmentation.  To do so, fully convolutional networks are used. Typical recognition nets take fixed-sized inputs and produce non-spatial outputs.  However, these fully connected layers can be viewed as convolutions with kernels that cover their entire input regions. Doing so casts them into fully convolutional networks that take input of any size and output classification maps. The computation is highly amortized over the overlapping regions of those patches.

Practically, contemporary classification networks are converted into fully convolutional networks and transfer their learned representations by fine-tuning to the segmentation task. 

Moreover, different approaches to improve the segmentations detail are presented. Their main proposal defines a skip architecture that combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer to produce accurate and detailed segmentations.  Also stride for their polling layers present a clear trade-off between definition and complexity.

Final results not only overcome previous state of the art results but also simplifies and speeds up learning and inference. 