# Dataset Description

## Overview
This project uses a curated dataset of **real semiconductor wafer and die inspection images** for Phase-1 validation of an Edge-AI defect classification system.  
The dataset is designed to demonstrate **feasibility, realism, and edge-deployment awareness**, rather than exhaustive coverage.

The final dataset contains **631 real images**, distributed across **8 fab-realistic defect classes**, with a clean train/validation/test split.

---

## Defect Classes and Image Counts

| Class | Total Images | Train | Validation | Test |
|-----|-------------|-------|------------|------|
| Clean | 100 | 70 | 15 | 15 |
| Other | 100 | 70 | 15 | 15 |
| CMP Scratches | 80 | 56 | 12 | 12 |
| Bridges | 76 | 53 | 11 | 12 |
| Cracks | 90 | 62 | 13 | 15 |
| Opens | 61 | 42 | 9 | 10 |
| Shorts | 60 | 42 | 9 | 9 |
| Malformed Vias | 65 | 45 | 9 | 11 |
| **Total** | **631** | — | — | — |

All images are **real inspection images**. No synthetic or organizer-provided images are included in the dataset.

---

## Data Sources

The dataset was assembled from multiple **public and academic sources**, selected to reflect realistic semiconductor inspection conditions:

- **Public Wafer Defect Datasets (e.g., WM-811K)**  
  Used for: `clean`, `shorts`, `opens`, `bridges`, `other`

- **Public SEM Defect Image Datasets (Roboflow / Zenodo)**  
  Used for: `cmp_scratches`, `cracks`, `other`

- **Curated Academic Literature (SEM Images)**  
  Used for: `malformed_vias`

All images were manually reviewed to ensure **one dominant defect per image**.

---

## Preprocessing
Before dataset splitting, all images were standardized using the following steps:

- Converted to **grayscale**
- Resized to a fixed input resolution
- Normalized for consistent intensity range
- Saved in PNG/JPEG format

Images with multiple defects, annotations, scale bars overlapping defects, or poor contrast were discarded.

---

## Dataset Split Strategy
The dataset was split at the image level using an approximate **70% / 15% / 15%** ratio:

- **Training set:** model learning
- **Validation set:** hyperparameter monitoring
- **Test set:** final evaluation

Care was taken to avoid data leakage across splits.

---

## Data Augmentation (Training Only)
To improve generalization and mitigate minor class imbalance, **on-the-fly data augmentation** was applied **only to the training set**.

Augmentation techniques:
- Small rotations and shifts (simulate inspection misalignment)
- Mild zoom (scale variation)
- Horizontal flip (orientation invariance)

The following were **explicitly avoided**:
- Vertical flips (physically unrealistic)
- Heavy geometric distortion
- Synthetic or GAN-generated defects

Augmented images were **not stored on disk** and were **not used** in validation or test sets.

---

## Ethical and Usage Notes
- Organizer-provided sample images were used **only for reference and visualization**
- No such images were used in training, validation, or testing
- All data usage complies with educational and research purposes

---

## Phase-2 Expansion Plan
In Phase-2, the dataset will be expanded with additional fab-like inspection images to:
- Increase coverage of rare defects
- Improve class balance
- Support on-device benchmarking and optimization
