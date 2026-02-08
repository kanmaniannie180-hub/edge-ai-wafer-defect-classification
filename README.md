# 🚀 Lightweight Edge‑AI System for Real‑Time Wafer & Die Defect Classification

> **Edge‑aware. Fab‑realistic. Deployment‑ready.**

This repository contains a **Phase‑1 prototype** of an **Edge‑AI defect classification system** designed for **real‑time semiconductor wafer and die inspection**. The solution uses a **lightweight CNN**, optimized for **CPU‑only edge deployment** on **NXP i.MX RT devices** via the **NXP eIQ framework**.

The objective is **not leaderboard accuracy** — it’s **technical credibility**: dataset realism, model feasibility, and edge‑deployment readiness.

---

## 📌 Problem Context

Modern semiconductor fabs generate **massive volumes of inspection images** (optical + SEM). Centralized pipelines struggle with:

* 🚫 High inference latency
* 🚫 Bandwidth overhead from image transfer
* 🚫 Poor scalability for real‑time production lines

**Edge‑based defect classification** enables **early screening directly at the inspection tool**, reducing **data movement**, **latency**, and **operational cost**.

This repo proves that concept — clean, simple, and edge‑aware.

---

## 🎯 Task Definition

* **Task Type:** Image Classification
* **Input:** Single grayscale wafer / die inspection image
* **Output:** One defect class label per image

📌 *Scope note:* This project focuses **strictly on classification** — **no detection or segmentation** in Phase‑1.

---

## ## 🧪 Defect Classes

The model classifies inspection images into **8 non-overlapping, fab-realistic defect categories**, chosen to be visually distinguishable and representative of common wafer and die-level failure modes.

**Final Class Set (Phase-1):**
1. `clean`
2. `other`
3. `shorts`
4. `opens`
5. `bridges`
6. `cmp_scratches`
7. `cracks`
8. `malformed_vias`

This class design balances **realistic semiconductor inspection scenarios** with **Phase-1 feasibility** and is intentionally scoped to scale in Phase-2.

<img width="1065" height="602" alt="image" src="https://github.com/user-attachments/assets/3653974b-8f62-4d25-bcc4-18841774508e" />

<img width="983" height="558" alt="image" src="https://github.com/user-attachments/assets/0d19d852-e414-40b6-a352-f2a9f5c57a3c" />

---

## 📂 Dataset

* **Minimum size:** 500+ images
* **Target size:** ~800 images
* **Class balance:** No class < 10%

### Data Sources

* WM‑811K Wafer Defect Dataset
* SEM defect image datasets
* Curated academic inspection imagery

### Preprocessing

All images are:

* Converted to **grayscale**
* Resized to a **fixed resolution**
* Manually curated to contain **one dominant defect per image**

📄 See **`DATASET.md`** for full provenance and curation details.

---

## 🧠 Model

* **Architecture:** Lightweight CNN

  * MobileNetV2 *or* EfficientNet‑Lite
* **Training Framework:** PyTorch
* **Export Format:** ONNX

### 🎯 Edge Constraints (Target)

| Constraint | Target                     |
| ---------- | -------------------------- |
| Model size | < 10 MB                    |
| Latency    | < 50 ms / image (CPU est.) |
| Deployment | NXP i.MX RT (CPU‑only)     |

The ONNX model is compatible with **NXP eIQ** for downstream deployment.

---

## 🗂 Repository Structure

```
├── dataset/
│   ├── train/
│   ├── val/
│   └── test/
├── models/
├── scripts/
├── train.py
├── eval.py
├── inference.py
├── export_onnx.py
├── DATASET.md
├── README.md
└── requirements.txt
```

Clean layout. No chaos. Easy handoff.

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model

```bash
python train.py
```

### 3️⃣ Evaluate the Model

```bash
python eval.py
```

### 4️⃣ Run Inference on a Sample Image

```bash
python inference.py --image path/to/image.png
```

### 5️⃣ Export to ONNX

```bash
python export_onnx.py
```

---

## 📊 Results (Phase‑1)

Phase‑1 evaluation prioritizes **feasibility and correctness**, not peak accuracy.

Reported metrics:

* Accuracy
* Macro Precision
* Macro Recall
* Confusion Matrix
* Model size

📄 Detailed results are documented in the **Phase‑1 submission PDF**.

---

## ⚠️ Limitations

Accepted (and intentional) Phase‑1 constraints:

* Limited dataset size vs. production fab data
* Latency is **estimated** (hardware benchmarking planned)
* Classification only (no localization)

This is a **proof‑of‑feasibility**, not a final fab product.

---

## 🛣 Phase‑2 Roadmap

* Deployment on **NXP i.MX RT hardware** using eIQ
* On‑device latency & memory benchmarking
* Incremental dataset expansion
* Optional defect localization extension

Translation: less theory, more silicon.

---

## 📎 Disclaimer

Organizer‑provided sample images are used **only for reference and visualization**. They are **not used** in training, validation, or testing.

---

## 🖼️ Visual Reference Policy (Phase-1)

For the purpose of **documentation clarity only**, representative images shown in this file may include:

* Organizer-provided sample images, **or**
* **Synthetic / illustrative placeholder images** generated solely for visualization

These images are **not** used in:

* Training
* Validation
* Testing

All models are trained and evaluated **exclusively on real inspection images** sourced as documented in `DATASET.md`.

---


## 📚 References

* WM‑811K Wafer Map Defect Dataset
* SEM Defect Image Datasets
* Academic literature on semiconductor inspection & edge AI(ieee or springer)

---

💡 *Built to prove that edge‑first inspection AI is not just possible — it’s practical.*
