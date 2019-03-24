### DEEPLAB summary 
__*Chen, Liang-Chieh, et al. "Rethinking atrous convolution for semantic image segmentation." arXiv preprint arXiv:1706.05587 (2017).*__

This paper revisit atours convolution, layers used in orther to adjust the filter's field of a view as well as control theresolution of feature responses

Deeplabv3+ framework uses an encoder-decoder structure. The authors have introduced the atrous separable convolution composed of a depthwise convolution (spatial convolution for each channel of the input) and pointwise convolution (1x1 convolution with the depthwise convolution as input).

They have used the DeepLabv3 framework as encoder. The most performant model has a modified Xception (F. Chollet (2017)) backbone with more layers, atrous depthwise separable convolutions instead of max pooling and batch normalization. The outputs of the ASPP are processed by a 1x1 convolution and upsampled by a factor of 4. The outputs of the encoder backbone CNN are also processed by another 1x1 convolution and concatenated to the previous ones. The feature maps feed two 3x3 convolutional layers and the outputs are upsampled by a factor of 4 to create the final segmented image.

The best DeepLabv3+ pretrained on the COCO and the JFT datasets has obtained a 89.0% mIoU score on the 2012 PASCAL VOC challenge. The model trained on the Cityscapes dataset has reached a 82.1% mIoU score for the associated challenge.