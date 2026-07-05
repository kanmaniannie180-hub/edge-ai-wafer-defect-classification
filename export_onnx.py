import torch

from model import create_model

import config

model = create_model()

checkpoint = torch.load(
    config.BEST_MODEL_PATH,
    map_location=config.DEVICE
)

model.load_state_dict(
    checkpoint["model_state_dict"]
)

model.eval()

dummy = torch.randn(
    1,
    3,
    config.IMAGE_SIZE,
    config.IMAGE_SIZE
).to(config.DEVICE)

torch.onnx.export(

    model,

    dummy,

    "pcb_defect_classifier.onnx",

    export_params=True,

    opset_version=17,

    input_names=["input"],

    output_names=["output"],

    dynamic_axes={
        "input": {0: "batch"},
        "output": {0: "batch"}
    }

)

print("ONNX model exported successfully.")