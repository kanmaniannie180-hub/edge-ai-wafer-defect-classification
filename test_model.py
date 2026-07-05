import torch

import config
from model import create_model


def main():

    model = create_model()

    print("Model Loaded Successfully!")

    x = torch.randn(
        2,
        3,
        config.IMAGE_SIZE,
        config.IMAGE_SIZE
    ).to(config.DEVICE)

    with torch.no_grad():
        y = model(x)

    print("Input :", x.shape)
    print("Output:", y.shape)
    print("Device:", next(model.parameters()).device)


if __name__ == "__main__":
    main()