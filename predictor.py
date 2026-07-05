"""
=========================================================
PCB Defect Predictor
Streamlit Dashboard Backend
=========================================================
"""

from __future__ import annotations

import sys
from pathlib import Path

# -------------------------------------------------------
# Add Project Root
# -------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# -------------------------------------------------------
# Imports
# -------------------------------------------------------

import torch
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms
import streamlit as st

import config
from model import create_model

from utils import (
    Timer,
    top_predictions
)

# -------------------------------------------------------
# Image Transform
# -------------------------------------------------------

transform = transforms.Compose([

    transforms.Resize(
        (config.IMAGE_SIZE, config.IMAGE_SIZE)
    ),

    transforms.ToTensor(),

    transforms.Normalize(

        mean=[0.485, 0.456, 0.406],

        std=[0.229, 0.224, 0.225]

    )

])

# -------------------------------------------------------
# Load Model (Cached)
# -------------------------------------------------------

@st.cache_resource(show_spinner=False)
def load_model():

    model = create_model()

    checkpoint = torch.load(

        config.BEST_MODEL_PATH,

        map_location=config.DEVICE

    )

    model.load_state_dict(

        checkpoint["model_state_dict"]

    )

    model.eval()

    return model


MODEL = load_model()

# -------------------------------------------------------
# Predictor Class
# -------------------------------------------------------

class PCBPredictor:

    def __init__(self):

        self.model = MODEL

        self.device = config.DEVICE

        self.class_names = config.CLASS_NAMES

    # ---------------------------------------------------
    # Preprocess Image
    # ---------------------------------------------------

    def preprocess(self, image: Image.Image):

        image = image.convert("RGB")

        tensor = transform(image)

        tensor = tensor.unsqueeze(0)

        return tensor.to(self.device)
        # ---------------------------------------------------
    # Predict
    # ---------------------------------------------------

    def predict(self, image: Image.Image):

        tensor = self.preprocess(image)

        with Timer() as timer:

            with torch.no_grad():

                outputs = self.model(tensor)

                probabilities = F.softmax(
                    outputs,
                    dim=1
                )[0]

        probs = probabilities.cpu().numpy()

        prediction_index = int(probs.argmax())

        predicted_class = self.class_names[
            prediction_index
        ]

        confidence = float(
            probs[prediction_index] * 100
        )

        top3 = top_predictions(

            probs,

            self.class_names,

            k=3

        )

        return {

            "prediction": predicted_class,

            "confidence": confidence,

            "probabilities": probs,

            "top3": top3,

            "inference_time": timer.elapsed_ms

        }

# -------------------------------------------------------
# Singleton Predictor
# -------------------------------------------------------

PREDICTOR = PCBPredictor()

# -------------------------------------------------------
# Public API
# -------------------------------------------------------

def predict_image(image: Image.Image):

    """
    Predict PCB defect from a PIL image.

    Returns:
        {
            prediction,
            confidence,
            probabilities,
            top3,
            inference_time
        }
    """

    return PREDICTOR.predict(image)