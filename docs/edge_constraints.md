## 🚀 Edge Constraints & Deployment Considerations

This project is designed with **edge deployment constraints** in mind, where compute, memory, and power resources are limited.  
All Phase-1 design decisions prioritize **feasibility, portability, and reliability** over aggressive optimization.

---

### 📦 Model Size & Efficiency
- **MobileNetV2** is selected due to its lightweight design and suitability for edge inference  
- Phase-1 uses a **frozen backbone with a compact classification head**, resulting in a small model footprint  

**Why this matters:**
- 🧠 Low parameter count  
- 💾 Reduced memory footprint  
- ⚡ Stable CPU-only inference  

---

### 🧮 Compute & Memory Constraints
- Edge devices typically operate with limited CPU capability and restricted RAM  
- MobileNetV2 leverages **depthwise separable convolutions**, which significantly reduce:
  - 🔽 Computational complexity  
  - 🔽 Memory access overhead  

Compared to standard CNNs, this makes the model well-suited for **embedded workloads**.

---

### ⏱️ Inference Latency Considerations
- The model is optimized for **inference**, enabling efficient forward passes for near real-time defect screening  
- Phase-1 focuses on:
  - ✅ Inference feasibility  
  - ✅ Architectural suitability for low-latency execution  

⏳ *Latency benchmarking and fine-grained optimization are intentionally deferred to later phases.*

---

### 🔄 Framework & Portability
- The trained TensorFlow model is exported to the **ONNX format**  
- ONNX enables inference using lightweight runtimes such as **ONNX Runtime**, providing:
  - 🔁 Framework-agnostic deployment  
  - 🌍 Portability across heterogeneous edge platforms  

This avoids dependency on a single deep learning framework.

---

### 🔌 Offline Execution
- The system supports **fully offline inference**, with all processing occurring locally on the device  
- This is critical for industrial inspection systems requiring:
  - 🕒 Deterministic latency  
  - 🛡️ High reliability  
  - 📍 Data locality  

---

### 🛠️ Phase-2 Optimization Scope
Future improvements in Phase-2 will include:
- 🔧 Selective model fine-tuning  
- 📉 Post-training quantization  
- ✂️ Pruning and operator-level optimization  

These optimizations aim to further reduce **latency and memory usage** while preserving **defect classification accuracy and recall**.
