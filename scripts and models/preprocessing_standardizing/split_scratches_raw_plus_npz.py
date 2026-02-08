import os
import zipfile
import shutil
import numpy as np
import cv2
import pandas as pd
from PIL import Image
from tqdm import tqdm

# ================== CONFIG ==================
RAW_ZIP = "scratches_raw.zip"
NPZ_PATH = "carinthia_scratches_50.npz"

CLASS_NAME = "scratches"

IMG_SIZE = (224, 224)
SEED = 42

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15
TEST_RATIO = 0.15

WORK_DIR = "tmp_scratches_mix"
BASE_OUT = "phase1_scratches_split"
# ============================================


def save_png(img_01, path):
    img_uint8 = (img_01 * 255).clip(0, 255).astype(np.uint8)
    Image.fromarray(img_uint8).save(path, format="PNG")


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

    # 🔑 conditional normalization
    if img.max() > 1.0:
        img = img / 255.0

    return img


def prepare_dirs():
    if os.path.exists(BASE_OUT):
        shutil.rmtree(BASE_OUT)

    for split in ["train", "val", "test"]:
        os.makedirs(os.path.join(BASE_OUT, split, "images"), exist_ok=True)


def load_raw_images():
    imgs, srcs = [], []

    with zipfile.ZipFile(RAW_ZIP, "r") as z:
        z.extractall(WORK_DIR)

    for root, _, files in os.walk(WORK_DIR):
        for f in files:
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".tiff")):
                path = os.path.join(root, f)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    imgs.append(img)
                    srcs.append(f"raw::{f}")

    return imgs, srcs


def load_npz_images():
    data = np.load(NPZ_PATH, allow_pickle=True)

    img_key = None
    for k in data.files:
        if data[k].ndim >= 3:
            img_key = k
            break

    if img_key is None:
        raise RuntimeError("No image array found in NPZ")

    imgs, srcs = [], []
    for i, img in enumerate(data[img_key]):
        imgs.append(img)
        srcs.append(f"npz::{i}")

    return imgs, srcs


def main():
    np.random.seed(SEED)
    prepare_dirs()

    raw_imgs, raw_src = load_raw_images()
    npz_imgs, npz_src = load_npz_images()

    images = raw_imgs + npz_imgs
    sources = raw_src + npz_src

    total = len(images)
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
            img = images[idx]
            src = sources[idx]

            std = standardize_image(img)
            fname = f"{CLASS_NAME}_{i:04d}.png"

            out_path = os.path.join(BASE_OUT, split, "images", fname)
            save_png(std, out_path)

            records.append({
                "source": src,
                "file": fname
            })

        pd.DataFrame(records).to_csv(
            os.path.join(BASE_OUT, split, "manifest.csv"),
            index=False
        )

    # -------- zip each split --------
    for split in ["train", "val", "test"]:
        zip_name = f"scratches_{split}.zip"
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
    print(" - scratches_train.zip")
    print(" - scratches_val.zip")
    print(" - scratches_test.zip")
    print("===================================")


if __name__ == "__main__":
    main()
