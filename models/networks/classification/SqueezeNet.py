import sys
from torch import nn
import torchvision.models.squeezenet as models
sys.path.append('../')
from models.networks.network import Net
import math

class SqueezeNet(Net):

    def __init__(self, cf, num_classes=21, pretrained=False, net_name='squeezenet'):
        super(AlexNet, self).__init__(cf)

        self.url = 'http://datasets.cvc.uab.es/models/pytorch/basic_vgg16.pth'
        self.pretrained = pretrained
        self.net_name = net_name

        self.model = models.squeezenet1_1(pretrained=self.pretrained, num_classes=num_classes)

        if pretrained:
            self.model.classifier[1] = nn.Conv2d(512, num_classes, kernel_size=(1,1), stride=(1,1))

    def forward(self, x):
        return self.model.forward(x)
