## 🧩 Final Problem Statement (Phase-1 Scope)

---

### 📌 Background
Semiconductor fabrication facilities rely on high-resolution inspection systems such as **optical inspection** and **scanning electron microscopy (SEM)** to identify wafer- and die-level defects.

These systems generate large volumes of inspection images, making centralized analysis pipelines prone to:
- High inference latency  
- Bandwidth bottlenecks  
- Increased infrastructure and operational cost  

Additionally, manual defect review limits scalability in high-throughput manufacturing environments.

To address these challenges, there is a need for a **real-time defect classification solution** that operates close to the inspection source.  
Deploying **lightweight deep learning models at the edge** enables fast screening while reducing data transfer, latency, and backend compute overhead.

---

### 🔒 Scope: Phase-1
Phase-1 focuses strictly on **feasibility, correctness, and edge-readiness**.

The objective is to build a **deployment-aware prototype** that respects embedded system constraints, without introducing unnecessary architectural or algorithmic complexity.

---

### 🔒 Task Definition
- **Task Type:** Image Classification  
- **Input:** Single inspection image  
- **Output:** One defect class label per image  

**Explicitly out of scope for Phase-1:**
- ❌ Object detection  
- ❌ Segmentation  
- ❌ Localization  

---

### 🔒 Defect Classes
The model classifies inspection images into **exactly eight non-overlapping categories**:
- clean  
- other  
- shorts  
- opens  
- bridges  
- cmp_scratches  
- cracks  
- malformed_vias  

These classes are selected to be **fab-realistic**, visually distinguishable, and scalable to future phases.

---

### 🔒 Input Constraints
- **Image Type:** Grayscale  
- **Channels:** 1 (replicated to 3 channels for CNN compatibility)  
- **Resolution:** Fixed (e.g., 224 × 224)  
- **Format:** PNG / JPEG  

📌 These constraints are aligned with the **memory, compute, and latency limitations** of embedded edge devices.

---

### 🔒 Edge Deployment Target
- **Target Device:** NXP i.MX RT series  
- **Inference Mode:** CPU-only  
- **Deployment Framework:** NXP eIQ  
- **Model Format:** ONNX-compatible  

---

### 🔒 Target Constraints (Phase-1 Design Envelope)

| Constraint           | Target (Estimated)            |
|----------------------|-------------------------------|
| Model Size           | < 10 MB                       |
| Inference Latency    | ~50 ms / image (CPU estimate) |
| Memory Footprint     | Edge-deployable on i.MX RT    |

These constraints define the **Phase-1 design envelope** and guide model architecture, preprocessing, and deployment decisions.

---

📍 *Future phases (Phase-2 / Phase-3) may extend this work toward on-device benchmarking, dataset expansion, and optional defect localization. These extensions are intentionally out of scope for Phase-1.*
