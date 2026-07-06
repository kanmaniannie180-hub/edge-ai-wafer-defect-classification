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

## Archtecture Diagram 

<img width="1536" height="1024" alt="ChatGPT Image Jul 5, 2026, 09_08_20 PM" src="https://github.com/user-attachments/assets/c07fa07d-325d-466f-a99d-9dedeb8502a3" />

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

See **dataset.md** for complete details.> 
**Dataset Organization:** The repository stores the processed dataset as separate `train`, `val`, and `test` directories at the repository root. This organization preserves the standard machine learning dataset split while simplifying repository navigation.

------------------------------------------------------------------------
## 📂 Dataset Structure

The processed dataset is organized into three standard machine learning splits:

```text
train/
val/
test/
```

Each split contains the same eight defect classes:

```text
train/
├── bridges/
├── clean/
├── cracks/
├── malformed_vias/
├── open/
├── other/
├── scratches/
└── short/

val/
├── bridges/
├── clean/
├── cracks/
├── malformed_vias/
├── open/
├── other/
├── scratches/
└── short/

test/
├── bridges/
├── clean/
├── cracks/
├── malformed_vias/
├── open/
├── other/
├── scratches/
└── short/
```

> **Repository Note:** For ease of browsing and GitHub repository management, the processed dataset splits (`train`, `val`, and `test`) are stored directly in the repository root rather than inside a separate `dataset/` directory. Together, these folders constitute the complete processed dataset used for training, validation, and testing.
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

##  System Workflow

<img width="1536" height="1024" alt="ChatGPT Image Jul 5, 2026, 09_15_39 PM" src="https://github.com/user-attachments/assets/170cd30d-8180-48a7-987c-ce44f0c874d3" />

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
------------------------------------------------------------------------
## Training Pipeline

<img width="1536" height="1024" alt="ChatGPT Image Jul 5, 2026, 09_13_32 PM" src="https://github.com/user-attachments/assets/f474a983-ce4b-4bbe-9abc-574c195fa713" />


------------------------------------------------------------------------

## 📈 Evaluation

``` bash
python evaluate.py
```


------------------------------------------------------------------------
##  Evaluation Pipeline


<img width="1536" height="1024" alt="ChatGPT Image Jul 5, 2026, 09_17_56 PM" src="https://github.com/user-attachments/assets/8631dbc4-fb0d-434c-99c0-41c59d381a63" />


------------------------------------------------------------------------

## 📦 Export ONNX

``` bash
python export_onnx.py
```

## 🖥 Streamlit Dashboard

``` bash
cd streamlit_app
streamlit run app.py
```

------------------------------------------------------------------------
###  Streamlit Deployment Architecture

<img width="1536" height="1024" alt="ChatGPT Image Jul 5, 2026, 09_17_56 PM" src="https://github.com/user-attachments/assets/73795cd7-ca6f-409b-84f6-29cd19aff011" />


------------------------------------------------------------------------
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
