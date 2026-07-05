import torch

import config
from model import create_model
from utils import (
    AverageMeter,
    calculate_accuracy,
    set_seed
)


def main():

    set_seed(config.SEED)

    meter = AverageMeter()

    meter.update(2.0)

    meter.update(4.0)

    print("Average:", meter.avg)

    outputs = torch.tensor([
        [0.1,0.9],
        [0.8,0.2]
    ])

    labels = torch.tensor([1,0])

    print("Accuracy:", calculate_accuracy(outputs, labels))

    model = create_model()

    print("Model Device:",
          next(model.parameters()).device)


if __name__ == "__main__":

    main()