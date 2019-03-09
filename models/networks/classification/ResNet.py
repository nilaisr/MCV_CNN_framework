import sys
from torch import nn
import torchvision.models.resnet as models
sys.path.append('../')
from models.networks.network import Net
import math

class ResNet(Net):

    def __init__(self, cf, num_classes=21, pretrained=False, net_name='resnet'):
        super(AlexNet, self).__init__(cf)

        self.url = 'http://datasets.cvc.uab.es/models/pytorch/basic_vgg16.pth'
        self.pretrained = pretrained
        self.net_name = net_name

        self.model = models.resnet152(pretrained=self.pretrained, num_classes=num_classes)

        if pretrained:
            self.model.fc = nn.Linear(512, num_classes)

    def forward(self, x):
        return self.model.forward(x)
