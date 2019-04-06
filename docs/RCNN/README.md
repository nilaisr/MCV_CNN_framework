### RCNN summary 
__*Girshick, Ross, et al. "Rich feature hierarchies for accurate object detection and semantic segmentation." Proceedings of the IEEE conference on computer vision and pattern recognition. 2014.*__

RCNN is an alternative to exhausitve search method of selective search for object recognition. The main idea that follows is that it generates random small regions in an image and merges them with a hierchical grouping. Thus the final group is a box containing the entire image. This merged works according to a similarity of color spaces and metrics. It returns some regions that proposes and object with some merged regions.

It uses deep learning in order to analize the object that the regions of selective search method returns. The input of the CNN is the resized  regions, so a 4096 dimensions vectors features are obtained. Those feature vector  are used to produce probabilities of belonging to one class or another. And alsow roks to feeds a linar regresor to adapt the shapes of the boundig box for a region proposal.

The CNN model described by the authors is trained on the 2012 ImageNet dataset of the original challenge of image classification. It is fine-tuned using the region proposals corresponding to an IoU greater than 0.5 with the ground-truth boxes. Two versions are produced, one version is using the 2012 PASCAL VOC dataset and the other the 2013 ImageNet dataset with bounding boxes.

