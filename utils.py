"""
=====================================================
Utility Functions
PCB Defect Streamlit Dashboard
=====================================================
"""

from __future__ import annotations

import io
import time
import base64
from pathlib import Path

import torch
from PIL import Image

# -------------------------------------------------------
# Root Directory
# -------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

# -------------------------------------------------------
# Timer
# -------------------------------------------------------

class Timer:

    def __enter__(self):

        self.start = time.perf_counter()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.end = time.perf_counter()

        self.elapsed_ms = (
            self.end - self.start
        ) * 1000

# -------------------------------------------------------
# Device Information
# -------------------------------------------------------

def get_device_information():

    if torch.cuda.is_available():

        props = torch.cuda.get_device_properties(0)

        return {

            "device": "CUDA",

            "gpu": props.name,

            "memory":

                round(props.total_memory / 1024**3,2),

            "cuda":

                torch.version.cuda

        }

    return {

        "device":"CPU",

        "gpu":"Not Available",

        "memory":0,

        "cuda":"None"

    }

# -------------------------------------------------------
# Convert Image to Bytes
# -------------------------------------------------------

def image_to_bytes(image:Image.Image):

    buffer = io.BytesIO()

    image.save(buffer,format="PNG")

    return buffer.getvalue()

# -------------------------------------------------------
# Image Base64
# -------------------------------------------------------

def image_to_base64(image:Image.Image):

    return base64.b64encode(

        image_to_bytes(image)

    ).decode()

# -------------------------------------------------------
# Badge Color
# -------------------------------------------------------

def badge_color(confidence):

    if confidence>=95:

        return "#00C853"

    elif confidence>=80:

        return "#64DD17"

    elif confidence>=60:

        return "#FFD600"

    elif confidence>=40:

        return "#FF9100"

    return "#D50000"

# -------------------------------------------------------
# Format Percentage
# -------------------------------------------------------

def percent(value):

    return f"{value:.2f}%"

# -------------------------------------------------------
# Top K Predictions
# -------------------------------------------------------

def top_predictions(probabilities,class_names,k=3):

    pairs = list(

        zip(class_names,probabilities)

    )

    pairs.sort(

        key=lambda x:x[1],

        reverse=True

    )

    return pairs[:k]

# -------------------------------------------------------
# Horizontal Progress Color
# -------------------------------------------------------

def progress_color(value):

    if value>90:

        return "🟢"

    elif value>70:

        return "🟡"

    return "🔴"

# -------------------------------------------------------
# Prediction Card Emoji
# -------------------------------------------------------

EMOJI = {

    "bridges":"🌉",

    "clean":"✅",

    "cracks":"⚡",

    "malformed_vias":"🕳️",

    "open":"📂",

    "other":"📦",

    "scratches":"🪛",

    "short":"🔌"

}

def get_emoji(cls):

    return EMOJI.get(cls,"📄")