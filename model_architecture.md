## 🏗️ Model Architecture Summary

The following table shows the architecture of the **trained Phase-1 baseline model**.

### Model: Sequential

| Layer (Type)              | Output Shape        | Parameters |
|---------------------------|---------------------|------------|
| Conv2D                    | (None, 222, 222, 32) | 896        |
| MaxPooling2D              | (None, 111, 111, 32) | 0          |
| Flatten                   | (None, 394,272)     | 0          |
| Dense (Output – 8 classes)| (None, 8)           | 3,154,184  |
| **Total Parameters**      | —                   | **3,155,082** |

---

### 📦 Model Size Details
- **Total Parameters:** 3,155,082  
- **Trainable Parameters:** 3,155,080  
- **Non-trainable Parameters:** 0  
- **ONNX Model Size:** **12.04 MB**

---

### 📝 Notes
- The architecture is intentionally **lightweight** to support edge deployment  
- Most parameters reside in the **final dense layer**, contributing to model compactness  
- This model serves as a **Phase-1 baseline**, focused on correctness and portability  
