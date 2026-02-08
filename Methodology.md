Methodology

This project follows a phase-based, reproducible methodology to establish a reliable baseline for wafer/SEM defect classification using Edge-AI principles.

1. Dataset Preparation

The dataset consists of eight defect classes, organized using a folder-based structure compatible with standard deep learning pipelines. Data was split into training, validation, and test sets, ensuring that each split contained the same set of classes. Labels were automatically inferred from directory names, eliminating manual labeling errors and ensuring consistency across experiments.

2. Model Architecture

A MobileNetV2 architecture pretrained on ImageNet was selected due to its lightweight design and suitability for edge deployment. The backbone was frozen to prevent overfitting and to establish a stable Phase-1 baseline. A custom classification head was added, consisting of:

Global Average Pooling

Dense layer with 128 units and ReLU activation

Output layer with 8 units and Softmax activation

3. Training Strategy

Training was conducted under strict constraints to avoid experimental bias:

Adam optimizer with a learning rate of 1e-4

Maximum of 25 epochs

Early stopping with a patience of 5

Data augmentation applied uniformly across all training classes

Validation and test datasets left unaugmented

No retraining loops or hyperparameter tuning were performed in Phase-1.

4. Evaluation

Model performance was evaluated on a held-out test set using:

Overall accuracy

Per-class precision

Per-class recall

Confusion matrix

Class-wise analysis was emphasized to understand defect-specific behavior rather than relying solely on aggregate accuracy.

5. Artifact Freezing

At the end of Phase-1, all outputs were frozen to ensure reproducibility. These include the trained model, evaluation metrics, confusion matrix visualization, and model size. Phase-1 artifacts are not modified in later phases.

6. ONNX Methodology

The trained TensorFlow model is exported to ONNX format using tf2onnx.

The ONNX model is validated using ONNX Runtime to ensure inference correctness.

ONNX enables framework-agnostic, edge-ready deployment with offline execution support.

7. Phase-2 Direction

Observed limitations, particularly in rare and visually ambiguous defect classes, guide Phase-2 work. Planned improvements include controlled fine-tuning, data balancing strategies, and edge-oriented optimizations.
