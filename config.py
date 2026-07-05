"""
=====================================================
PCB Defect Classification - Configuration File
Model : ConvNeXt Tiny
Framework : PyTorch
=====================================================
"""

from pathlib import Path
import torch

# =====================================================
# PROJECT PATHS
# =====================================================

PROJECT_ROOT = Path(__file__).parent

DATASET_DIR = PROJECT_ROOT / "dataset"

TRAIN_DIR = DATASET_DIR / "train"
VAL_DIR = DATASET_DIR / "val"
TEST_DIR = DATASET_DIR / "test"

CHECKPOINT_DIR = PROJECT_ROOT / "checkpoints"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

CHECKPOINT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# =====================================================
# DATASET
# =====================================================

CLASS_NAMES = [
    "bridges",
    "clean",
    "cracks",
    "malformed_vias",
    "open",
    "other",
    "scratches",
    "short"
]

NUM_CLASSES = len(CLASS_NAMES)

# =====================================================
# IMAGE SETTINGS
# =====================================================

IMAGE_SIZE = 224

# =====================================================
# TRAINING
# =====================================================

BATCH_SIZE = 16

NUM_EPOCHS = 60

LEARNING_RATE = 1e-4

WEIGHT_DECAY = 1e-4

NUM_WORKERS = 0

# =====================================================
# DEVICE
# =====================================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# =====================================================
# RANDOM SEED
# =====================================================

SEED = 42

# =====================================================
# MODEL SAVE PATH
# =====================================================

BEST_MODEL_PATH = CHECKPOINT_DIR / "best_model.pth"

LAST_MODEL_PATH = CHECKPOINT_DIR / "last_model.pth"

# =====================================================
# EARLY STOPPING
# =====================================================

PATIENCE = 8

# =====================================================
# LABEL SMOOTHING
# =====================================================

LABEL_SMOOTHING = 0.1