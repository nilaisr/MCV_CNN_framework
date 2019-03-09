import sys
from torch import nn
import torchvision.models.inception as models
sys.path.append('../')
from models.networks.network import Net
import math

class Inception(Net):

    def __init__(self, cf, num_classes=21, pretrained=False, net_name='inception'):
        super(AlexNet, self).__init__(cf)

        self.url = 'http://datasets.cvc.uab.es/models/pytorch/basic_vgg16.pth'
        self.pretrained = pretrained
        self.net_name = net_name

        self.model = models.inception_v3(pretrained=self.pretrained, num_classes=num_classes)

        if pretrained:
            self.model.AuxLogits.fc = nn.Linear(768, num_classes)
            self.model.fc = nn.Linear(2048, num_classes)

    def forward(self, x):
        return self.model.forward(x)
