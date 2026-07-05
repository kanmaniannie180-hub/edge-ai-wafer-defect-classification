"""
=====================================================
Dataset Loader
=====================================================
"""

import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

import config


# -----------------------------
# Training Transformations
# -----------------------------
train_transform = transforms.Compose([
    transforms.RandomResizedCrop(
    config.IMAGE_SIZE,
    scale=(0.8, 1.0)
    ),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(5),
    transforms.RandomAffine(
        degrees=0,
        translate=(0.05, 0.05)
    ),
    transforms.ColorJitter(
        brightness=0.15,
        contrast=0.15
    ),
    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# -----------------------------
# Validation/Test Transformations
# -----------------------------
test_transform = transforms.Compose([
    transforms.Resize((config.IMAGE_SIZE, config.IMAGE_SIZE)),
    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# -----------------------------
# Datasets
# -----------------------------
train_dataset = datasets.ImageFolder(
    config.TRAIN_DIR,
    transform=train_transform
)

val_dataset = datasets.ImageFolder(
    config.VAL_DIR,
    transform=test_transform
)

test_dataset = datasets.ImageFolder(
    config.TEST_DIR,
    transform=test_transform
)

# -----------------------------
# DataLoaders
# -----------------------------
train_loader = DataLoader(
    train_dataset,
    batch_size=config.BATCH_SIZE,
    shuffle=True,
    num_workers=config.NUM_WORKERS,
    pin_memory=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=config.BATCH_SIZE,
    shuffle=False,
    num_workers=config.NUM_WORKERS,
    pin_memory=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=config.BATCH_SIZE,
    shuffle=False,
    num_workers=config.NUM_WORKERS,
    pin_memory=True
)