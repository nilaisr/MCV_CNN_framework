### Inception-v4 summary

__*Szegedy, Christian, et al. "Inception-v4, inception-resnet and the impact of residual connections on learning." Thirty-First AAAI Conference on Artificial Intelligence. 2017.*__
 
Google Inc presents their latest revisions of the Inception architecture (Beginning with Inception-v4 and forward). These models are compared and combined with ResNet approaches to quantify the effect of residual connections and their benefits on very deep neural network classification models.
 
First, comparing Inception-v4 with previous inception models, it implements a more uniform simplified architecture and a greater number of inception modules.  This was achieved partly because the migration to a TensorFlow framework which allowed for a simpler deployment of the training model. 
 
Second, ResNet authors argued that residual connections are inherently necessary for training very deep convolutional models. Google experiments demonstrate that it is not very difficult to train very deep competitive models without using them. However residual connections seem to improve the training speed greatly. 
 
Finally, Google combines both architectures, they are named Inception-Resnet models. It was found that models following this architecture exceeding 1000 filters behaves unstably in training even with very low learning rate values. It could be mitigating by scaling down the residuals before adding them to the previous layer. 
 
As a result, google concludes that their two new models, Inception-v4 and Incpetion-ResNet-v2 obtained roughly the same recognition performance and outperformed previous models. Moreover, the use of residual connections leads to dramatically improved training speed for the Inception architecture. 
