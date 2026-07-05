import torch
from model import create_model

model = create_model()

total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(
    p.numel() for p in model.parameters()
    if p.requires_grad
)

with open("model_summary.txt", "w") as f:

    f.write("PCB Defect Classification Model\n")
    f.write("="*50 + "\n\n")

    f.write(f"Architecture : ConvNeXt Tiny\n")
    f.write(f"Total Parameters : {total_params:,}\n")
    f.write(f"Trainable Parameters : {trainable_params:,}\n")

print("Model summary saved.")