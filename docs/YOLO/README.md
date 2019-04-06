### YOLO summary 
__*Redmon, Joseph, et al. "You only look once: Unified, real-time object detection." Proceedings of the IEEE conference on computer vision and pattern recognition. 2016.*__

YOLO predicts bounding boxes and class probability directly with a single netweok that alows the model predict in real time.

With an image as an input, it divides the regions with grids, each of them were predicted by one cell in order to found bounding bouxes with a confidence score. This score tells the probability to detect the object multipy by the IoU between the predicted and the ground truth.

The CNN used is inspired by the GoogLeNet model introducing the inception modules. The network has 24 convolutional layers followed by 2 fully-connected layers. The final layer outputs a  tensor corresponding to the predictions for each cell of the grid. C is the number of estimated probabilities for each class. B is the fixed number of anchor boxes per cell, each of these boxes being related to 4 coordinates (coordinates of the center of the box, width and height) and a confidence value.

The YOLO model however predicts a high number of bounding boxes. Thus there are a lot of bounding boxes without any object. The Non-Maximum Suppression (NMS) method is applied at the end of the network. It consists in merging highly-overlapping bounding boxes of a same object into a single one. The authors noticed that there are still few false positive detected.