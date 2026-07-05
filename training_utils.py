"""
=====================================================
Utility Functions
PCB Defect Classification
=====================================================
"""

import random
import numpy as np
import torch


# ---------------------------------------------------
# Set Random Seed
# ---------------------------------------------------

def set_seed(seed):

    random.seed(seed)

    np.random.seed(seed)

    torch.manual_seed(seed)

    torch.cuda.manual_seed_all(seed)

    torch.backends.cudnn.deterministic = True

    torch.backends.cudnn.benchmark = False


# ---------------------------------------------------
# Average Meter
# ---------------------------------------------------

class AverageMeter:

    def __init__(self):

        self.reset()

    def reset(self):

        self.sum = 0.0

        self.count = 0

        self.avg = 0.0

    def update(self, value, n=1):

        self.sum += value * n

        self.count += n

        self.avg = self.sum / self.count


# ---------------------------------------------------
# Accuracy
# ---------------------------------------------------

def calculate_accuracy(outputs, labels):

    _, preds = torch.max(outputs, 1)

    correct = (preds == labels).sum().item()

    return correct / labels.size(0)


# ---------------------------------------------------
# Save Checkpoint
# ---------------------------------------------------

def save_checkpoint(model, optimizer, epoch, path):

    torch.save({

        "epoch": epoch,

        "model_state_dict": model.state_dict(),

        "optimizer_state_dict": optimizer.state_dict()

    }, path)


# ---------------------------------------------------
# Early Stopping
# ---------------------------------------------------

class EarlyStopping:

    def __init__(self, patience=8):

        self.patience = patience

        self.counter = 0

        self.best_loss = float("inf")

        self.stop = False

    def __call__(self, val_loss):

        if val_loss < self.best_loss:

            self.best_loss = val_loss

            self.counter = 0

        else:

            self.counter += 1

            if self.counter >= self.patience:

                self.stop = True