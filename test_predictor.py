from pathlib import Path
from PIL import Image

from predictor import predict_image

# -------------------------------------------------------
# Dataset Path
# -------------------------------------------------------

TEST_DIR = Path("../dataset/test")

# -------------------------------------------------------
# Warm-up GPU
# -------------------------------------------------------

print("=" * 60)
print("GPU Warm-up...")
print("=" * 60)

first_image = next(TEST_DIR.rglob("*.png"))

_ = predict_image(Image.open(first_image))

print("Warm-up completed.\n")

# -------------------------------------------------------
# Test
# -------------------------------------------------------

correct = 0
total = 0

print("=" * 90)

for class_folder in sorted(TEST_DIR.iterdir()):

    if not class_folder.is_dir():
        continue

    print(f"\nClass : {class_folder.name}")

    images = sorted(class_folder.glob("*.png"))[:5]   # Test first 5 images

    for img_path in images:

        image = Image.open(img_path)

        result = predict_image(image)

        prediction = result["prediction"]

        confidence = result["confidence"]

        inference = result["inference_time"]

        correct_flag = prediction == class_folder.name

        if correct_flag:
            correct += 1

        total += 1

        symbol = "✅" if correct_flag else "❌"

        print(
            f"{symbol} {img_path.name:20s}"
            f" GT={class_folder.name:15s}"
            f" Pred={prediction:15s}"
            f" Conf={confidence:6.2f}%"
            f" Time={inference:7.2f} ms"
        )

print("\n" + "=" * 90)

accuracy = correct / total * 100

print(f"Correct Predictions : {correct}")
print(f"Total Images        : {total}")
print(f"Sample Accuracy     : {accuracy:.2f}%")

print("=" * 90)