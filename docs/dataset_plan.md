# 🔒 Dataset Requirements & Curation Plan (Phase-1)

This document defines the **locked dataset requirements**, **approved data sources**, and **curation rules** for the Phase-1 wafer/die defect classification task.

The goal is to ensure **dataset credibility, class balance, and judge-defensible provenance**, rather than maximizing dataset size.

---

## 📌 Dataset Requirements (Locked)

* **Total images:** Minimum 500, target 800
* **Number of classes:** 8 (finalized)
* **Class balance:** No class < 10% of total dataset
* **Labeling rule:** One image = one dominant defect
* **Restriction:** Organizer-provided images are **not used** in training, validation, or testing

---

## 📊 Target Class Distribution

| Class          | Target Images |
| -------------- | ------------- |
| clean          | 100           |
| other          | 100           |
| shorts         | 100           |
| opens          | 100           |
| bridges        | 100           |
| cmp_scratches  | 100           |
| cracks         | 100           |
| malformed_vias | 100           |
| **Total**      | **800**       |

📌 *If even 60–80 images per class are achieved, the dataset is still considered acceptable for Phase-1. The above table represents the ideal target.*

---

## 🧠 Data Sources (Approved & Defensible)

### SOURCE 1 — Public Wafer Defect Datasets (Primary)

**Dataset:** WM-811K (Wafer Map Defect Dataset)

**Used for classes:**

* `clean`
* `shorts`
* `opens`
* `bridges`
* `other`

**Why it is accepted:**

* Widely cited in academic literature
* Fab-realistic defect patterns
* Publicly available with clear licensing

⚠️ *Limitation:* Wafer maps are not SEM images. This limitation is explicitly acknowledged and documented.

---

### SOURCE 2 — SEM Defect Datasets (Secondary)

**Source:** Roboflow / publicly available SEM inspection datasets

**Used for classes:**

* `cmp_scratches`
* `cracks`
* `other`

**Explicit exclusion:**

* `shorts`, `opens`, `bridges`

📌 *Reason:* SEM imagery lacks direct electrical connectivity context, making it unsuitable for connectivity-based defect classes.

This demonstrates **technical understanding**, not dataset convenience.

---

### SOURCE 3 — Curated Academic Images (Limited & Manual)

**Used for class:**

* `malformed_vias`

**Curation method:**

* Extract figures from peer-reviewed academic papers
* Crop to a single dominant defect
* Remove annotations, arrows, and scale bars

**Why this is allowed:**

* Educational, non-commercial use
* Images are transformed and curated
* Original sources are cited

---

## 🧼 Data Cleaning & Standardization Plan

All images are processed using a **single standardized pipeline**:

* Converted to **grayscale**
* Resized to **224 × 224**
* Normalized to **[0, 1]** intensity range
* Saved as **PNG / JPEG**

### Discard Rules

Images are discarded if they contain:

* ❌ Multiple defects
* ❌ Annotations, arrows, or labels
* ❌ Mixed magnification levels
* ❌ Low contrast or excessive blur

📌 *Quality is prioritized over quantity.*

---

## 🔁 Data Augmentation (Train Set Only)

Augmentation is applied **only to the training set** and **only to improve class balance**, not to inflate dataset size.

### Allowed

* Rotation (±15°)
* Horizontal / vertical flips
* Light Gaussian noise
* Minor contrast adjustment

### Not Allowed

* ❌ GAN-generated images
* ❌ Heavy geometric distortions
* ❌ Synthetic textures or structures

📌 *Synthetic defect generation is intentionally excluded for Phase-1.*

---

## 🔀 Dataset Split Strategy

* **Train:** 70%
* **Validation:** 15%
* **Test:** 15%

### Split Rules

* No data leakage across splits
* Augmented images remain **only** in the training set
* Images from the same original source are not reused in validation or test

---

## 📁 Final Dataset Structure

```
dataset/
├── train/
├── val/
└── test/
    ├── clean/
    ├── other/
    ├── shorts/
    ├── opens/
    ├── bridges/
    ├── cmp_scratches/
    ├── cracks/
    └── malformed_vias/
```


---

## 📄 Mandatory Disclosure Statement

> **“Organizer-provided sample images are used strictly for reference and class understanding and are not included in training, validation, or testing datasets.”**

This statement is included verbatim to ensure **transparency and compliance**.

---

✅ *This dataset plan prioritizes credibility, reproducibility, and Phase-1 feasibility over scale or novelty.*
