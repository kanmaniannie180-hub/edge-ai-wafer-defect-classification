import os
import zipfile
import shutil
import numpy as np
import cv2
import pandas as pd
from PIL import Image
from tqdm import tqdm

# ================== CONFIG ==================
RAW_ZIP = "open_raw.zip"
CLASS_NAME = "open"

IMG_SIZE = (224, 224)
SEED = 42

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15

WORK_DIR = "tmp_open_raw"
BASE_OUT = "phase1_open_split"
# ============================================


def save_png(img_01, path):
    img_uint8 = (img_01 * 255).clip(0, 255).astype(np.uint8)
    Image.fromarray(img_uint8).save(path, format="PNG")


def standardize_image(img):
    img = np.asarray(img)

    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = img.astype(np.float32)
    img = cv2.resize(img, IMG_SIZE, interpolation=cv2.INTER_LINEAR)

    # conditional normalization (NO black images)
    if img.max() > 1.0:
        img = img / 255.0

    return img


def prepare_dirs():
    if os.path.exists(BASE_OUT):
        shutil.rmtree(BASE_OUT)

    for split in ["train", "val", "test"]:
        os.makedirs(os.path.join(BASE_OUT, split, "images"), exist_ok=True)


def main():
    np.random.seed(SEED)
    prepare_dirs()

    with zipfile.ZipFile(RAW_ZIP, "r") as z:
        z.extractall(WORK_DIR)

    image_files = []
    for root, _, files in os.walk(WORK_DIR):
        for f in files:
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".tiff")):
                image_files.append(os.path.join(root, f))

    total = len(image_files)
    indices = np.arange(total)
    np.random.shuffle(indices)

    n_train = int(total * TRAIN_RATIO)
    n_val = int(total * VAL_RATIO)

    splits = {
        "train": indices[:n_train],
        "val": indices[n_train:n_train + n_val],
        "test": indices[n_train + n_val:]
    }

    for split, idxs in splits.items():
        records = []

        for i, idx in enumerate(tqdm(idxs, desc=f"saving {split}")):
            path = image_files[idx]
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

            std = standardize_image(img)
            fname = f"{CLASS_NAME}_{i:04d}.png"

            out_path = os.path.join(BASE_OUT, split, "images", fname)
            save_png(std, out_path)

            records.append({
                "source_file": os.path.basename(path),
                "file": fname
            })

        pd.DataFrame(records).to_csv(
            os.path.join(BASE_OUT, split, "manifest.csv"),
            index=False
        )

    for split in ["train", "val", "test"]:
        zip_name = f"open_{split}.zip"
        zip_path = os.path.join(BASE_OUT, zip_name)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            split_dir = os.path.join(BASE_OUT, split)
            for root, _, files in os.walk(split_dir):
                for f in files:
                    full = os.path.join(root, f)
                    arc = os.path.relpath(full, split_dir)
                    z.write(full, arcname=arc)

    shutil.rmtree(WORK_DIR, ignore_errors=True)

    print("===================================")
    print(f"Total images: {total}")
    print(f"Train: {len(splits['train'])}")
    print(f"Val:   {len(splits['val'])}")
    print(f"Test:  {len(splits['test'])}")
    print("Zips created:")
    print(" - open_train.zip")
    print(" - open_val.zip")
    print(" - open_test.zip")
    print("===================================")


if __name__ == "__main__":
    main()
