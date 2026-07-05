import dataset

def main():

    print("Train Images :", len(dataset.train_dataset))
    print("Validation Images :", len(dataset.val_dataset))
    print("Test Images :", len(dataset.test_dataset))

    print()

    print("Classes")
    print(dataset.train_dataset.classes)

    print()

    images, labels = next(iter(dataset.train_loader))

    print("Image Batch Shape :", images.shape)
    print("Label Shape :", labels.shape)


if __name__ == "__main__":
    main()