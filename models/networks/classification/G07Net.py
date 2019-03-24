import sys
from torch import nn
import torchvision.models.vgg as models
sys.path.append('../')
from models.networks.network import Net
import math

class G07Net(Net):

    def __init__(self, cf, num_classes=21, pretrained=False, net_name='vgg16'):
        super(VGG16, self).__init__(cf)

        self.url = 'http://datasets.cvc.uab.es/models/pytorch/basic_vgg16.pth'
        self.pretrained = pretrained
        self.net_name = net_name

        self.model = models.vgg16(pretrained=False, num_classes=num_classes)

        self.features = nn.Sequential(

            nn.Conv2d(3, 16, kernel_size=2, padding=1, stride=2),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(),

            nn.Conv2d(16, 16, kernel_size=2, padding=1, stride=2),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(),
            nn.Conv2d(16, 32, kernel_size=2, padding=1, stride=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(),

            nn.Conv2d(32, 64, kernel_size=2, padding=1, stride=2),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(),
            nn.Conv2d(64, 64, kernel_size=2, padding=1, stride=1),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(),

            nn.MaxPool2d(kernel_size=8, stride=None),
        )

        self.classifier = nn.Sequential(
            # Block: classifier
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes)
        )

        '''if pretrained:
            self.load_basic_weights(net_name)
        else:
            self._initialize_weights()'''

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)

        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                m.weight.data.normal_(0, 0.01)
                m.bias.data.zero_()
