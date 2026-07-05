"""
=====================================================
Train Script
PCB Defect Classification
=====================================================
"""

import torch
import json
import torch.nn as nn

import config
import dataset

from model import create_model

from trainer import (
    train_one_epoch,
    validate_one_epoch,
    freeze_backbone,
    unfreeze_backbone
)

from utils import (
    set_seed,
    EarlyStopping,
    save_checkpoint
)

# ---------------------------------------------------
# Set Random Seed
# ---------------------------------------------------

set_seed(config.SEED)

# ---------------------------------------------------
# Create Model
# ---------------------------------------------------

model = create_model()

# ---------------------------------------------------
# Freeze Backbone Initially
# ---------------------------------------------------

freeze_backbone(model)

# ---------------------------------------------------
# Loss Function
# ---------------------------------------------------

criterion = nn.CrossEntropyLoss(
    label_smoothing=config.LABEL_SMOOTHING
)

# ---------------------------------------------------
# Optimizer
# ---------------------------------------------------

optimizer = torch.optim.AdamW(

    filter(
        lambda p: p.requires_grad,
        model.parameters()
    ),

    lr=config.LEARNING_RATE,

    weight_decay=config.WEIGHT_DECAY

)

# ---------------------------------------------------
# Scheduler
# ---------------------------------------------------

scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(

    optimizer,

    T_max=config.NUM_EPOCHS

)

# ---------------------------------------------------
# AMP
# ---------------------------------------------------

scaler = torch.amp.GradScaler(
    enabled=config.DEVICE.type == "cuda"
)

# ---------------------------------------------------
# Early Stopping
# ---------------------------------------------------

early_stopping = EarlyStopping(
    patience=config.PATIENCE
)

# ---------------------------------------------------
# Best Accuracy
# ---------------------------------------------------

best_accuracy = 0.0
train_losses = []
train_accs = []

val_losses = []
val_accs = []
# ---------------------------------------------------
# Training Loop
# ---------------------------------------------------

for epoch in range(config.NUM_EPOCHS):

    print("\n" + "=" * 60)

    print(f"Epoch {epoch + 1}/{config.NUM_EPOCHS}")

    print("=" * 60)

    # -----------------------------------------------
    # Unfreeze Backbone after 10 epochs
    # -----------------------------------------------

    if epoch == 10:

        print("\nUnfreezing ConvNeXt Backbone...\n")

        unfreeze_backbone(model)

        optimizer = torch.optim.AdamW(

            model.parameters(),

            lr=1e-5,

            weight_decay=config.WEIGHT_DECAY

        )

        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(

            optimizer,

            T_max=config.NUM_EPOCHS - epoch

        )

    # -----------------------------------------------
    # Train
    # -----------------------------------------------

    train_loss, train_acc = train_one_epoch(

        model,

        dataset.train_loader,

        criterion,

        optimizer,

        scaler

    )

    # -----------------------------------------------
    # Validation
    # -----------------------------------------------

    val_loss, val_acc = validate_one_epoch(

        model,

        dataset.val_loader,

        criterion

    )

# Save history
    train_losses.append(train_loss)
    train_accs.append(train_acc)

    val_losses.append(val_loss)
    val_accs.append(val_acc)

    scheduler.step()

    # -----------------------------------------------
    # Print Metrics
    # -----------------------------------------------

    print()

    print(f"Train Loss : {train_loss:.4f}")

    print(f"Train Acc  : {train_acc*100:.2f}%")

    print()

    print(f"Val Loss   : {val_loss:.4f}")

    print(f"Val Acc    : {val_acc*100:.2f}%")

    print()

    print(f"Learning Rate : {scheduler.get_last_lr()[0]:.8f}")

    # -----------------------------------------------
    # Save Last Model
    # -----------------------------------------------

    save_checkpoint(

        model,

        optimizer,

        epoch,

        config.LAST_MODEL_PATH

    )
    # -----------------------------------------------
    # Save Best Model
    # -----------------------------------------------

    if val_acc > best_accuracy:

        best_accuracy = val_acc

        save_checkpoint(

            model,

            optimizer,

            epoch,

            config.BEST_MODEL_PATH

        )

        print()

        print("✅ Best Model Saved")

    # -----------------------------------------------
    # Early Stopping
    # -----------------------------------------------

    early_stopping(val_loss)

    if early_stopping.stop:

        print()

        print("Early Stopping Triggered")

        break
print()

print("=" * 60)

print("Training Completed")

print("=" * 60)

print()

print(f"Best Validation Accuracy : {best_accuracy*100:.2f}%")

print()

print("Best Model:")

print(config.BEST_MODEL_PATH)

print()

print("Last Model:")

print(config.LAST_MODEL_PATH)

# -----------------------------------------------
# Save Training History
# -----------------------------------------------


history = {

    "train_loss": train_losses,

    "train_acc": train_accs,

    "val_loss": val_losses,

    "val_acc": val_accs

}

with open("history.json", "w") as f:

    json.dump(history, f, indent=4)

print()

print("✅ Training history saved to history.json")