"""
=====================================================
PCB Defect Classification
ConvNeXt Tiny
=====================================================
"""

import torch.nn as nn
from torchvision.models import convnext_tiny
from torchvision.models import ConvNeXt_Tiny_Weights

import config


class PCBClassifier(nn.Module):

    def __init__(self):

        super().__init__()

        self.model = convnext_tiny(
            weights=ConvNeXt_Tiny_Weights.DEFAULT
        )

        # Freeze backbone
        for param in self.model.features.parameters():
            param.requires_grad = False

        in_features = self.model.classifier[2].in_features

        self.model.classifier = nn.Sequential(

            nn.Flatten(),

            nn.LayerNorm(in_features),

            nn.Dropout(0.5),

            nn.Linear(in_features, 512),

            nn.GELU(),

            nn.Dropout(0.3),

            nn.Linear(512, config.NUM_CLASSES)
        )

    def forward(self, x):

        return self.model(x)


def create_model():

    model = PCBClassifier()

    return model.to(config.DEVICE)