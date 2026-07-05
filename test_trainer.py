import torch
import torch.nn as nn

from model import create_model
import dataset

from trainer import train_one_epoch

model = create_model()

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=1e-4
)

scaler = torch.amp.GradScaler(
    enabled=True
)

loss, acc = train_one_epoch(
    model,
    dataset.train_loader,
    criterion,
    optimizer,
    scaler
)

print()

print("Loss :", loss)

print("Accuracy :", acc)