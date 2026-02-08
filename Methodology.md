## 🧠 Methodology

This project follows a **phase-based, reproducible methodology** to establish a reliable **Phase-1 baseline** for wafer / SEM defect classification using **Edge-AI principles**.

---

### 📂 1. Dataset Preparation
The dataset consists of **eight defect classes**, organized using a folder-based structure compatible with standard deep learning pipelines.

**Key steps:**
- 📁 Class-wise directory organization  
- 🔀 Train / Validation / Test split with identical class sets  
- 🏷️ Labels automatically inferred from directory names  

This approach eliminates manual labeling errors and ensures **consistent, repeatable experiments**.

---

### 🏗️ 2. Model Architecture
A **MobileNetV2** architecture pretrained on ImageNet is selected for its lightweight design and suitability for edge deployment.

**Architecture strategy:**
- 🔒 Backbone frozen to prevent overfitting  
- 🎯 Stable Phase-1 baseline  
- ➕ Custom classification head added  

**Classification head:**
- Global Average Pooling  
- Dense layer (128 units, ReLU)  
- Output layer (8 units, Softmax)  

---

### ⚙️ 3. Training Strategy
Training is conducted under **strict constraints** to avoid experimental bias and ensure reproducibility.

**Configuration:**
- 🔧 Optimizer: Adam  
- 📉 Learning rate: 1e-4  
- 🔁 Max epochs: 25  
- ⏹️ Early stopping (patience = 5)  

**Data handling:**
- 🔄 Uniform data augmentation applied to the training set  
- 🚫 Validation and test sets left unaugmented  

❌ No hyperparameter tuning or retraining loops were performed in Phase-1.

---

### 📊 4. Evaluation
Model performance is evaluated on a **held-out test set** using:
- 📈 Overall accuracy  
- 🎯 Per-class precision  
- 🔍 Per-class recall  
- 🧩 Confusion matrix  

Class-wise analysis is emphasized to understand **defect-specific behavior**, rather than relying solely on aggregate accuracy.

---

### 📌 5. Artifact Freezing (Phase-1)
At the end of Phase-1, all outputs are **frozen** to ensure reproducibility.

**Frozen artifacts include:**
- 💾 Trained model  
- 📊 Evaluation metrics  
- 🧩 Confusion matrix visualization  
- 📦 Model size  

Phase-1 artifacts are **not modified** in later phases.

---

### 🔄 6. ONNX Methodology
To support edge deployment and portability:
- 🔁 The trained TensorFlow model is exported to **ONNX** using `tf2onnx`  
- ✅ The ONNX model is validated using **ONNX Runtime**  
- 🌍 ONNX enables framework-agnostic, offline, edge-ready deployment  

---

### 🛠️ 7. Phase-2 Direction
Observed limitations—particularly in **rare and visually ambiguous defect classes**—guide Phase-2 efforts.

**Planned improvements include:**
- 🔧 Controlled fine-tuning of the backbone  
- ⚖️ Data balancing strategies  
- ⚡ Edge-oriented optimizations (quantization, pruning)  

These enhancements aim to improve **defect recall and inference efficiency** while preserving **edge feasibility**.
