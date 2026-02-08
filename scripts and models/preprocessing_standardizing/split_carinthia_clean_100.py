import os
import zipfile
import numpy as np
import cv2
import pandas as pd
from PIL import Image
from tqdm import tqdm
import shutil

# ================== CONFIG ==================
NPZ_PATH = "carinthia_clean_100.npz"
CLASS_NAME = "clean"

IMG_SIZE = (224, 224)
SEED = 42

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15

BASE_OUT = "phase1_clean_split"
# ============================================


def force_image_2d(img):
    img = np.asarray(img)
    img = np.squeeze(img)

    if img.ndim == 1:
        side = int(np.sqrt(img.size))
        if side * side != img.size:
            raise ValueError("flattened image not square")
        img = img.reshape(side, side)

    if img.ndim != 2:
        raise ValueError(f"invalid ndim: {img.ndim}")

    return img


def standardize_image(img):
    img = force_image_2d(img)
    img = img.astype(np.float32)

    img = cv2.resize(img, IMG_SIZE, interpolation=cv2.INTER_LINEAR)

    # 🔑 FIX: conditional normalization
    if img.max() > 1.0:
        img = img / 255.0

    return img



def save_png(img_01, path):
    img_uint8 = (img_01 * 255).clip(0, 255).astype(np.uint8)
    Image.fromarray(img_uint8).save(path, format="PNG")


def prepare_dirs():
    if os.path.exists(BASE_OUT):
        shutil.rmtree(BASE_OUT)

    for split in ["train", "val", "test"]:
        os.makedirs(os.path.join(BASE_OUT, split, "images"), exist_ok=True)


def main():
    np.random.seed(SEED)
    prepare_dirs()

    data = np.load(NPZ_PATH, allow_pickle=True)

    img_key = None
    for k in data.files:
        if data[k].ndim >= 3:
            img_key = k
            break

    if img_key is None:
        raise RuntimeError("No image array found in NPZ")

    images = data[img_key]
    total = len(images)

    indices = np.arange(total)
    np.random.shuffle(indices)

    n_train = int(total * TRAIN_RATIO)
    n_val = int(total * VAL_RATIO)
    n_test = total - n_train - n_val

    splits = {
        "train": indices[:n_train],
        "val": indices[n_train:n_train + n_val],
        "test": indices[n_train + n_val:]
    }

    for split, idxs in splits.items():
        records = []

        for i, idx in enumerate(tqdm(idxs, desc=f"saving {split}")):
            img = images[idx]
            std = standardize_image(img)

            fname = f"{CLASS_NAME}_{i:04d}.png"
            out_path = os.path.join(BASE_OUT, split, "images", fname)
            save_png(std, out_path)

            records.append({
                "original_index": int(idx),
                "file": fname
            })

        pd.DataFrame(records).to_csv(
            os.path.join(BASE_OUT, split, "manifest.csv"),
            index=False
        )

    # zip each split
    for split in ["train", "val", "test"]:
        zip_name = f"clean_{split}.zip"
        zip_path = os.path.join(BASE_OUT, zip_name)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            split_dir = os.path.join(BASE_OUT, split)
            for root, _, files in os.walk(split_dir):
                for f in files:
                    full = os.path.join(root, f)
                    arc = os.path.relpath(full, split_dir)
                    z.write(full, arcname=arc)

    print("===================================")
    print(f"Total images: {total}")
    print(f"Train: {n_train}")
    print(f"Val:   {n_val}")
    print(f"Test:  {n_test}")
    print("Zips created:")
    print(" - clean_train.zip")
    print(" - clean_val.zip")
    print(" - clean_test.zip")
    print("===================================")


if __name__ == "__main__":
    main()
