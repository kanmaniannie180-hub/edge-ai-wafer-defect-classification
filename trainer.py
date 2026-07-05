"""
=====================================================
Trainer
PCB Defect Classification
=====================================================
"""

import torch
from tqdm import tqdm

import config
from utils import AverageMeter, calculate_accuracy


# =====================================================
# Freeze Backbone
# =====================================================

def freeze_backbone(model):

    for param in model.model.features.parameters():
        param.requires_grad = False


# =====================================================
# Unfreeze Backbone
# =====================================================

def unfreeze_backbone(model):

    for param in model.model.features.parameters():
        param.requires_grad = True


# =====================================================
# Train One Epoch
# =====================================================

def train_one_epoch(
    model,
    loader,
    criterion,
    optimizer,
    scaler
):

    model.train()

    loss_meter = AverageMeter()
    acc_meter = AverageMeter()

    progress = tqdm(loader)

    for images, labels in progress:

        images = images.to(config.DEVICE, non_blocking=True)
        labels = labels.to(config.DEVICE, non_blocking=True)

        optimizer.zero_grad(set_to_none=True)

        with torch.amp.autocast(
            device_type="cuda",
            enabled=config.DEVICE.type == "cuda"
        ):

            outputs = model(images)

            loss = criterion(outputs, labels)

        scaler.scale(loss).backward()

        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )

        scaler.step(optimizer)
        scaler.update()

        acc = calculate_accuracy(outputs, labels)

        loss_meter.update(loss.item(), images.size(0))
        acc_meter.update(acc, images.size(0))

        progress.set_description(

            f"Train | "
            f"Loss {loss_meter.avg:.4f} | "
            f"Acc {acc_meter.avg:.4f}"

        )

    return loss_meter.avg, acc_meter.avg


# =====================================================
# Validation
# =====================================================

@torch.no_grad()

def validate_one_epoch(
    model,
    loader,
    criterion
):

    model.eval()

    loss_meter = AverageMeter()
    acc_meter = AverageMeter()

    progress = tqdm(loader)

    for images, labels in progress:

        images = images.to(config.DEVICE, non_blocking=True)
        labels = labels.to(config.DEVICE, non_blocking=True)

        with torch.amp.autocast(
            device_type="cuda",
            enabled=config.DEVICE.type == "cuda"
        ):

            outputs = model(images)

            loss = criterion(outputs, labels)

        acc = calculate_accuracy(outputs, labels)

        loss_meter.update(loss.item(), images.size(0))
        acc_meter.update(acc, images.size(0))

        progress.set_description(

            f"Valid | "
            f"Loss {loss_meter.avg:.4f} | "
            f"Acc {acc_meter.avg:.4f}"

        )

    return loss_meter.avg, acc_meter.avg