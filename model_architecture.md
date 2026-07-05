# 🏗️ Model Architecture

The PCB Defect Classification system is built using **ConvNeXt Tiny**, a modern convolutional neural network architecture pretrained on **ImageNet**. Instead of training from scratch, the project applies **transfer learning**, replacing the original classification head with a custom classifier designed for the eight PCB defect classes.

The feature extraction backbone is initially frozen during training to preserve pretrained representations. After the initial training phase, the backbone is unfrozen for fine-tuning, allowing the model to adapt to the PCB inspection dataset while reducing the risk of overfitting.

---

## Model Pipeline

```text
Input Image (224 × 224 × 3)
            │
            ▼
Image Preprocessing
(Resize + Normalize)
            │
            ▼
ConvNeXt Tiny Backbone
(ImageNet Pretrained)
            │
            ▼
Global Feature Extraction
            │
            ▼
Flatten
            │
            ▼
Layer Normalization
            │
            ▼
Dropout (0.5)
            │
            ▼
Linear Layer
768 → 512
            │
            ▼
GELU Activation
            │
            ▼
Dropout (0.3)
            │
            ▼
Linear Layer
512 → 8
            │
            ▼
Softmax Prediction
```

---

## Model Summary

| Component | Description |
|------------|-------------|
| Backbone | ConvNeXt Tiny |
| Pretrained Weights | ImageNet |
| Framework | PyTorch |
| Input Resolution | 224 × 224 × 3 |
| Number of Classes | 8 |
| Classifier Head | Fully Connected Neural Network |
| Activation | GELU |
| Regularization | Dropout (0.5, 0.3) |
| Normalization | LayerNorm |
| Output | 8-Class Softmax Probability Distribution |

---

## Transfer Learning Strategy

The training process was performed in two stages.

### Stage 1 — Feature Extraction

- ConvNeXt Tiny backbone frozen
- Only the classification head was trained
- Faster convergence
- Reduced overfitting on the small dataset

### Stage 2 — Fine-Tuning

- Entire network unfrozen
- Low learning rate used for fine-tuning
- Improved feature adaptation for PCB defects

---

## Training Configuration

| Hyperparameter | Value |
|---------------|------:|
| Optimizer | AdamW |
| Learning Rate | 1e-4 |
| Fine-tuning Learning Rate | 1e-5 |
| Scheduler | Cosine Annealing LR |
| Batch Size | 16 |
| Epochs | 60 |
| Early Stopping Patience | 8 |
| Loss Function | CrossEntropy Loss + Label Smoothing |
| Mixed Precision | Automatic Mixed Precision (AMP) |

---

## Model Characteristics

- Modern ConvNeXt Tiny architecture
- ImageNet transfer learning
- Lightweight classifier head
- Automatic mixed precision training
- GPU acceleration (CUDA)
- ONNX export supported
- Designed for real-time PCB defect classification

---

## Future Improvements

Potential enhancements include:

- Larger PCB inspection dataset
- Hyperparameter optimization
- Model quantization
- TensorRT optimization
- Edge-device deployment
- Knowledge distillation for lightweight inference
