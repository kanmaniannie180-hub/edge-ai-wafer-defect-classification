import os

TRAIN_DIR = r"D:\PCB_Defect_EdgeAI\dataset\train"

print("=" * 60)
print("Training Dataset Statistics")
print("=" * 60)

total = 0

classes = sorted(os.listdir(TRAIN_DIR))

for cls in classes:

    folder = os.path.join(TRAIN_DIR, cls)

    if not os.path.isdir(folder):
        continue

    count = 0

    for file in os.listdir(folder):

        if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            count += 1

    total += count

    print(f"{cls:<20} : {count}")

print("=" * 60)
print(f"Total Images : {total}")