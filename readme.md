# 🚀 Edge AI PCB Defect Classification using ConvNeXt Tiny

> **A Transfer Learning--based PCB Defect Classification System with
> PyTorch, ONNX Export, and an Interactive Streamlit Dashboard**

------------------------------------------------------------------------

## 📖 Overview

This project presents a deep learning--based **PCB defect classification
system** built using **ConvNeXt Tiny** and **transfer learning**. It
provides an end-to-end workflow for training, evaluation, inference,
ONNX export, and deployment through an interactive **Streamlit
dashboard**.

The project demonstrates a production-style computer vision pipeline for
automated optical inspection (AOI), enabling fast and accurate
classification of common PCB manufacturing defects.

------------------------------------------------------------------------

## ✨ Features

-   ConvNeXt Tiny (ImageNet Pretrained)
-   Transfer Learning
-   PyTorch Training Pipeline
-   Automatic Data Augmentation
-   AdamW Optimizer
-   Cosine Annealing LR Scheduler
-   Label Smoothing
-   Early Stopping
-   Mixed Precision (AMP)
-   Confusion Matrix
-   Precision, Recall & F1-Score
-   ONNX Export
-   GPU Acceleration
-   Interactive Streamlit Dashboard
-   Real-Time PCB Defect Prediction
-   Downloadable Prediction Report

------------------------------------------------------------------------

## 🧠 Model

  Property       Value
  -------------- --------------------------------
  Architecture   ConvNeXt Tiny
  Framework      PyTorch
  Input Size     224 × 224
  Classes        8
  Optimizer      AdamW
  Scheduler      Cosine Annealing LR
  Loss           CrossEntropy + Label Smoothing

------------------------------------------------------------------------

## 📂 Dataset

The dataset contains **632 real PCB inspection images** distributed
across **8 defect classes**.

  Split          Images
  ------------ --------
  Training          440
  Validation         93
  Testing            99
  Total             632

See **dataset.md** for complete details.

------------------------------------------------------------------------

## 🏗 Project Structure

``` text
PCB_Defect_EdgeAI/
├── checkpoints/
├── dataset/
├── outputs/
├── streamlit_app/
├── config.py
├── dataset.py
├── model.py
├── train.py
├── trainer.py
├── evaluate.py
├── predict.py
├── export_onnx.py
├── benchmark.py
├── utils.py
├── requirements.txt
├── README.md
└── dataset.md
```

------------------------------------------------------------------------

## ⚙️ Installation

``` bash
git clone <repository-url>
cd PCB_Defect_EdgeAI
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🚀 Training

``` bash
python train.py
```

## 📈 Evaluation

``` bash
python evaluate.py
```

## 📦 Export ONNX

``` bash
python export_onnx.py
```

## 🖥 Streamlit Dashboard

``` bash
cd streamlit_app
streamlit run app.py
```

### Dashboard Features

-   Upload PCB Image
-   Real-Time Prediction
-   Confidence Score
-   Top-3 Predictions
-   Probability Distribution
-   Confidence Gauge
-   GPU Information
-   Download Prediction Report

------------------------------------------------------------------------

## 📊 Results

  Metric                         Value
  -------------------------- ---------
  Best Validation Accuracy      72.04%
  Classes                            8
  Framework                    PyTorch

------------------------------------------------------------------------

## 🔮 Future Work

-   Larger dataset
-   Better class balance
-   TensorRT optimization
-   Edge deployment
-   Model quantization

------------------------------------------------------------------------

## 📚 Technologies

-   Python
-   PyTorch
-   Torchvision
-   Streamlit
-   ONNX
-   Plotly
-   Pandas
-   NumPy

------------------------------------------------------------------------

## 📄 License

This project is intended for educational, research, and demonstration
purposes.

------------------------------------------------------------------------

## 👩‍💻 Author

**Annie Darling Kanmani**

B.Tech Artificial Intelligence & Data Science

⭐ If you found this project useful, consider giving it a star on
GitHub.
