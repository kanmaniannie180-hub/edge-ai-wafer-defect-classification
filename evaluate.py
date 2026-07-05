"""
=====================================================
PCB Defect Evaluation
IEEE Paper Evaluation Pipeline
=====================================================
"""

import os

import torch
import pandas as pd

from model import create_model

import config
import dataset

print("="*60)
print("Loading Best Model...")
print("="*60)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model = create_model()

checkpoint = torch.load(
    config.BEST_MODEL_PATH,
    map_location=config.DEVICE
)

model.load_state_dict(
    checkpoint["model_state_dict"]
)

model.eval()

print("✓ Model Loaded")

# ---------------------------------------------------
# Containers
# ---------------------------------------------------

image_names = []

true_labels = []

predicted_labels = []

prediction_scores = []

print("\nRunning inference...\n")

# ---------------------------------------------------
# Inference
# ---------------------------------------------------

with torch.no_grad():

    index = 0

    for images, labels in dataset.test_loader:

        images = images.to(config.DEVICE)

        outputs = model(images)

        probabilities = torch.softmax(outputs, dim=1)

        confidence, predictions = torch.max(probabilities, dim=1)

        predicted_labels.extend(
            predictions.cpu().numpy()
        )

        true_labels.extend(
            labels.cpu().numpy()
        )

        prediction_scores.extend(
            confidence.cpu().numpy()
        )

        batch_size = images.size(0)

        for i in range(batch_size):

            image_names.append(
                f"image_{index}.png"
            )

            index += 1

print()

print("="*60)
print("Inference Finished")
print("="*60)

print()

print("Total Test Images :", len(image_names))
# =====================================================
# IEEE Evaluation Metrics
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

print("\nGenerating Evaluation Metrics...\n")

# -----------------------------------------------------
# Overall Metrics
# -----------------------------------------------------

accuracy = accuracy_score(
    true_labels,
    predicted_labels
)

precision = precision_score(
    true_labels,
    predicted_labels,
    average="macro",
    zero_division=0
)

recall = recall_score(
    true_labels,
    predicted_labels,
    average="macro",
    zero_division=0
)

f1 = f1_score(
    true_labels,
    predicted_labels,
    average="macro",
    zero_division=0
)

print(f"Accuracy  : {accuracy*100:.2f}%")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

# -----------------------------------------------------
# Metrics TXT
# -----------------------------------------------------

with open("metrics.txt","w") as file:

    file.write("PCB Defect Classification Results\n")
    file.write("="*40 + "\n\n")

    file.write(f"Accuracy  : {accuracy*100:.2f}%\n")
    file.write(f"Precision : {precision:.4f}\n")
    file.write(f"Recall    : {recall:.4f}\n")
    file.write(f"F1 Score  : {f1:.4f}\n")

print("✓ metrics.txt saved")

# -----------------------------------------------------
# Classification Report
# -----------------------------------------------------

class_names = dataset.train_dataset.classes

report = classification_report(
    true_labels,
    predicted_labels,
    target_names=class_names,
    output_dict=True,
    zero_division=0
)

report_df = pd.DataFrame(report).transpose()

report_df.to_csv(
    "classification_report.csv",
    index=True
)

print("✓ classification_report.csv saved")

# -----------------------------------------------------
# Per Class Metrics
# -----------------------------------------------------

per_class = report_df.iloc[:-3][
    ["precision","recall","f1-score","support"]
]

per_class.to_csv(
    "per_class_metrics.csv"
)

print("✓ per_class_metrics.csv saved")

# -----------------------------------------------------
# Save Predictions
# -----------------------------------------------------

results = pd.DataFrame({

    "Image": image_names,

    "Ground Truth": [
        class_names[i]
        for i in true_labels
    ],

    "Prediction": [
        class_names[i]
        for i in predicted_labels
    ],

    "Confidence": prediction_scores

})

results.to_csv(
    "inference_results.csv",
    index=False
)

print("✓ inference_results.csv saved")

# -----------------------------------------------------
# Confusion Matrix
# -----------------------------------------------------

cm = confusion_matrix(
    true_labels,
    predicted_labels
)

plt.figure(figsize=(12,10))

sns.heatmap(

    cm,

    annot=True,

    fmt="d",

    cmap="Blues",

    xticklabels=class_names,

    yticklabels=class_names

)

plt.xlabel(
    "Predicted Class",
    fontsize=13
)

plt.ylabel(
    "Actual Class",
    fontsize=13
)

plt.title(
    "Confusion Matrix",
    fontsize=16,
    weight="bold"
)

plt.xticks(rotation=30)

plt.yticks(rotation=0)

plt.tight_layout()

plt.savefig(

    "confusion_matrix.png",

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("✓ confusion_matrix.png saved")
# =====================================================
# Training Curves
# =====================================================

import json

print("\nGenerating Training Curves...\n")

with open("history.json", "r") as file:

    history = json.load(file)

train_loss = history["train_loss"]
val_loss = history["val_loss"]

train_acc = history["train_acc"]
val_acc = history["val_acc"]

epochs = range(1, len(train_loss)+1)

# -----------------------------------------------------
# Loss Curve
# -----------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    epochs,
    train_loss,
    linewidth=2,
    label="Training Loss"
)

plt.plot(
    epochs,
    val_loss,
    linewidth=2,
    label="Validation Loss"
)

plt.xlabel("Epoch", fontsize=13)
plt.ylabel("Loss", fontsize=13)

plt.title(
    "Training vs Validation Loss",
    fontsize=16,
    weight="bold"
)

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    "loss_curve.png",
    dpi=300
)

plt.close()

print("✓ loss_curve.png saved")

# -----------------------------------------------------
# Accuracy Curve
# -----------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    epochs,
    np.array(train_acc)*100,
    linewidth=2,
    label="Training Accuracy"
)

plt.plot(
    epochs,
    np.array(val_acc)*100,
    linewidth=2,
    label="Validation Accuracy"
)

plt.xlabel("Epoch", fontsize=13)
plt.ylabel("Accuracy (%)", fontsize=13)

plt.title(
    "Training vs Validation Accuracy",
    fontsize=16,
    weight="bold"
)

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    "accuracy_curve.png",
    dpi=300
)

plt.close()

print("✓ accuracy_curve.png saved")

# -----------------------------------------------------
# Precision Recall F1 Graph
# -----------------------------------------------------

metrics = per_class

plt.figure(figsize=(12,7))

x = np.arange(len(metrics))

width = 0.25

plt.bar(
    x-width,
    metrics["precision"],
    width,
    label="Precision"
)

plt.bar(
    x,
    metrics["recall"],
    width,
    label="Recall"
)

plt.bar(
    x+width,
    metrics["f1-score"],
    width,
    label="F1 Score"
)

plt.xticks(
    x,
    metrics.index,
    rotation=30
)

plt.ylabel("Score")

plt.ylim(0,1.05)

plt.title(
    "Per-Class Precision / Recall / F1",
    fontsize=16,
    weight="bold"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "precision_recall_f1.png",
    dpi=300
)

plt.close()

print("✓ precision_recall_f1.png saved")

# =====================================================
# Final Summary
# =====================================================

print("\n" + "="*60)
print("Evaluation Completed Successfully")
print("="*60)

print(f"\nOverall Accuracy : {accuracy*100:.2f}%")
print(f"Macro Precision : {precision:.4f}")
print(f"Macro Recall    : {recall:.4f}")
print(f"Macro F1 Score  : {f1:.4f}")

print("\nGenerated Files")

files = [

    "metrics.txt",

    "classification_report.csv",

    "per_class_metrics.csv",

    "inference_results.csv",

    "confusion_matrix.png",

    "loss_curve.png",

    "accuracy_curve.png",

    "precision_recall_f1.png"

]

for file in files:

    print("✓", file)