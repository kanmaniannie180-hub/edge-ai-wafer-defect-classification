# edge-ai-wafer-defect-classification
Lightweight Edge-AI system for real-time wafer and die inspection defect classification using a CNN optimized for NXP i.MX RT devices.

Edge-AI Wafer Defect Classification

Overview:

This repository contains a Phase-1 prototype of an Edge-AI based defect classification system for semiconductor wafer and die inspection images.
The goal is to demonstrate dataset credibility, model feasibility, and edge-awareness rather than state-of-the-art accuracy.

The system classifies inspection images into fab-realistic defect categories using a lightweight CNN suitable for deployment on NXP i.MX RT edge devices via the NXP eIQ framework.

Problem Context:

Modern semiconductor fabrication relies on optical and SEM inspection systems that generate large volumes of high-resolution images.
Centralized inspection pipelines suffer from:

High inference latency

Bandwidth overhead due to image transfer

Poor scalability for real-time production lines

Edge-based defect classification enables early defect screening at the inspection tool, reducing data movement and operational cost.

Task Definition:

Task: Image Classification

Input: Single grayscale wafer / die inspection image

Output: One defect class label per image

This project focuses strictly on classification (no detection or segmentation).

Defect Classes

The model classifies images into 8 non-overlapping classes:

clean

other

shorts

opens

bridges

cmp_scratches

cracks

malformed_vias

These classes are chosen to be visually distinguishable, fab-realistic, and scalable to later phases.

Dataset:

Minimum 500+ images (target: 800)

Balanced class distribution (no class <10%)

Images sourced from:

Public wafer defect datasets (e.g., WM-811K)

SEM defect datasets

Curated academic inspection images

All images are:

Converted to grayscale

Resized to a fixed resolution

Manually curated to contain one dominant defect per image

📄 See DATASET.md for full dataset details and provenance.

Model

Architecture: Lightweight CNN (MobileNetV2 / EfficientNet-Lite)

Training Framework: PyTorch

Export Format: ONNX

Edge Constraints (Target)

Model size: < 10 MB

Inference latency: < 50 ms / image (CPU estimate)

Deployment target: NXP i.MX RT (CPU-only)

The model is exported in ONNX format for compatibility with NXP eIQ.

Repository Structure
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

How to Run:

1. Install Dependencies
pip install -r requirements.txt

2. Train the Model
python train.py

3. Evaluate the Model
python eval.py

4. Run Inference on a Sample Image
python inference.py --image path/to/image.png

5. Export Model to ONNX
python export_onnx.py

Results (Phase-1):

Phase-1 evaluation focuses on feasibility and correctness, not peak accuracy.

Reported metrics include:

Accuracy

Precision (macro)

Recall (macro)

Confusion Matrix

Model size

Detailed results are documented in the Phase-1 submission PDF.

Limitations:

Dataset size is limited compared to production-scale fab data

Latency is estimated (hardware benchmarking planned in Phase-2)

Model is trained for classification only (no localization)

These limitations are intentionally accepted for Phase-1.

Phase-2 Roadmap:

Deployment on NXP i.MX RT hardware using eIQ

Latency and memory benchmarking on device

Incremental dataset expansion

Optional defect localization extension

Disclaimer:

Organizer-provided sample images are used only for reference and visualization.
They are not used in training, validation, or testing.

References:

WM-811K Wafer Map Defect Dataset

SEM Defect Image Datasets

Academic literature on semiconductor inspection and edge AI
