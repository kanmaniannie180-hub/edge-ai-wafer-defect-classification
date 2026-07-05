# Dataset Description

# Overview

This project uses a curated dataset of **real PCB defect inspection images** for training and evaluating a deep learning–based defect classification system using **ConvNeXt Tiny** and **PyTorch**.

The dataset contains **632 real images**, categorized into **8 PCB defect classes**, and is organized into separate training, validation, and testing subsets following a **70% / 15% / 15%** split.

The dataset was prepared to simulate real-world automated optical inspection (AOI) scenarios and supports transfer learning for industrial PCB defect classification.

---

# Dataset Statistics

| Class | Total | Train | Validation | Test |
|--------|------:|------:|-----------:|-----:|
| Bridges | 76 | 53 | 11 | 12 |
| Clean | 100 | 70 | 15 | 15 |
| Cracks | 90 | 62 | 13 | 15 |
| Malformed Vias | 65 | 45 | 9 | 11 |
| Open | 61 | 42 | 9 | 10 |
| Other | 100 | 70 | 15 | 15 |
| Scratches | 80 | 56 | 12 | 12 |
| Short | 60 | 42 | 9 | 9 |
| **Total** | **632** | **440** | **93** | **99** |

---

# Dataset Directory Structure

```text
dataset/
│
├── train/
│   ├── bridges/
│   ├── clean/
│   ├── cracks/
│   ├── malformed_vias/
│   ├── open/
│   ├── other/
│   ├── scratches/
│   └── short/
│
├── val/
│   ├── bridges/
│   ├── clean/
│   ├── cracks/
│   ├── malformed_vias/
│   ├── open/
│   ├── other/
│   ├── scratches/
│   └── short/
│
└── test/
    ├── bridges/
    ├── clean/
    ├── cracks/
    ├── malformed_vias/
    ├── open/
    ├── other/
    ├── scratches/
    └── short/
```

---

# Defect Classes

The dataset contains the following PCB defect categories:

- Bridges
- Clean
- Cracks
- Malformed Vias
- Open
- Other
- Scratches
- Short

Each image belongs to **exactly one class**, making the problem a **multi-class image classification task**.

---

# Data Sources

The dataset was curated from multiple publicly available academic and industrial resources to represent realistic PCB inspection scenarios.

Sources include:

- Public PCB defect datasets
- Academic research datasets
- Open-source inspection image repositories
- Public benchmark datasets used for computer vision research

All images were manually reviewed to ensure that a single dominant defect was present before inclusion in the dataset.

---

# Data Preprocessing

During training, images are processed using the PyTorch `torchvision` pipeline.

### Training Transformations

- Random Resized Crop
- Random Horizontal Flip
- Small Random Rotation
- Random Affine Translation
- Color Jitter (Brightness & Contrast)
- Conversion to Tensor
- ImageNet Normalization

Validation and testing images undergo only:

- Resize to **224 × 224**
- Tensor conversion
- ImageNet normalization

This ensures that validation and test metrics remain unbiased.

---

# Data Augmentation

Data augmentation is applied **only to the training dataset** to improve model generalization.

The augmentation pipeline includes:

- Random resized cropping
- Horizontal flipping
- Small-angle rotation
- Minor affine translation
- Brightness variation
- Contrast variation

No augmentation is applied during validation or testing.

---

# Dataset Split

The dataset is divided using an approximate **70% / 15% / 15%** ratio.

| Split | Images |
|--------|-------:|
| Training | 440 |
| Validation | 93 |
| Testing | 99 |

The split ensures that images from one subset do not appear in another, preventing data leakage.

---

# Model Compatibility

The dataset is designed for transfer learning with modern CNN architectures.

This project uses:

- ConvNeXt Tiny
- Image Size: **224 × 224**
- RGB Images
- ImageNet Pretrained Weights

The preprocessing pipeline is fully compatible with PyTorch's pretrained ConvNeXt models.

---

# Limitations

Although the dataset represents realistic PCB inspection conditions, several limitations remain:

- Moderate class imbalance
- Limited dataset size
- Some visually similar defect categories (e.g., Open vs Short)
- Performance may improve with additional industrial inspection images

---

# Future Improvements

Future versions of the dataset may include:

- Additional PCB defect categories
- Larger industrial datasets
- Better class balance
- Higher-resolution inspection images
- More diverse manufacturing conditions
- Multi-label defect annotations

---

# License

This dataset is provided solely for educational, research, and demonstration purposes.

Users should ensure compliance with the licensing terms of the original data sources before commercial use.
