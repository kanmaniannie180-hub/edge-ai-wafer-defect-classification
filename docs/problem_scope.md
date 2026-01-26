# 🧩 Final Problem Statement (Phase‑1 Scope)

## 📌 Background

Semiconductor fabrication facilities rely on **high‑resolution inspection systems** such as **optical inspection** and **scanning electron microscopy (SEM)** to identify wafer‑ and die‑level defects.

These inspection tools generate **large volumes of image data**, making centralized inspection pipelines prone to:

* High inference latency
* Bandwidth bottlenecks
* Increased operational and infrastructure cost

In addition, **manual defect review** limits scalability in **high‑throughput manufacturing environments**.

There is a clear need for a **real‑time, scalable defect classification solution** that operates **close to the inspection source**.

Deploying **lightweight deep learning models on edge devices** enables **fast defect screening**, while significantly reducing **data transfer, latency, and backend compute overhead**.

---

## 🔒 Scope: Phase‑1

Phase‑1 focuses strictly on **feasibility, correctness, and edge‑readiness**.

This phase intentionally avoids complex tasks in favor of a **well‑scoped, deployment‑aware prototype** that aligns with **embedded system constraints**.

---

## 🔒 Task Definition

* **Task Type:** Image Classification
* **Input:** Single inspection image
* **Output:** One defect class label per image

### Explicitly Out of Scope for Phase‑1

* ❌ Object detection
* ❌ Segmentation
* ❌ Localization

---

## 🔒 Defect Classes

The model classifies inspection images into **exactly eight non‑overlapping defect categories**:

* `clean`
* `other`
* `shorts`
* `opens`
* `bridges`
* `cmp_scratches`
* `cracks`
* `malformed_vias`

These classes are selected to be **fab‑realistic**, **visually distinguishable**, and **scalable to future phases**.

---

## 🔒 Input Constraints

* **Image Type:** Grayscale
* **Channels:** 1
* **Resolution:** Fixed (e.g., 224 × 224)
* **Format:** PNG / JPEG

📌 *These constraints are aligned with the memory, compute, and latency limitations of embedded edge devices.*

---

## 🔒 Edge Deployment Target

* **Target Device:** NXP i.MX RT series
* **Inference Mode:** CPU‑only
* **Deployment Framework:** NXP eIQ
* **Model Format:** ONNX‑compatible

---

## 🔒 Target Constraints

| Constraint        | Target                         |
| ----------------- | ------------------------------ |
| Model Size        | < 10 MB                        |
| Inference Latency | < 50 ms / image (CPU estimate) |
| Memory Footprint  | Edge‑deployable on i.MX RT     |

These constraints define the **design envelope for Phase‑1** and directly guide **model architecture, preprocessing, and deployment decisions**.

---

📍 *Future phases (Phase‑2 / Phase‑3) may extend this work toward on‑device benchmarking, dataset expansion, and optional defect localization. These extensions are intentionally **out of scope** for
