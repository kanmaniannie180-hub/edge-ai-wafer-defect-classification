"""
=========================================================
PCB Defect Classification Dashboard
=========================================================
"""

from pathlib import Path
import sys
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import config

from predictor import predict_image

from charts import (
    confidence_gauge,
    probability_chart,
    top3_chart
)

from ui import (
    page_header,
    prediction_card,
    metrics_row,
    device_card,
    model_card,
    top3_table,
    footer
)

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(

    page_title="PCB Defect Detection",

    page_icon="🔍",

    layout="wide"

)

# ----------------------------------------------------
# Load CSS
# ----------------------------------------------------

css_file = Path(__file__).parent / "style.css"

if css_file.exists():

    with open(css_file) as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )

# ----------------------------------------------------
# Header
# ----------------------------------------------------

page_header()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.title("Dashboard")

    model_card()

    st.divider()

    device_card()

    st.divider()

    st.write("### Model")

    st.write("ConvNeXt Tiny")

    st.write("Transfer Learning")

    st.write("Input Size")

    st.write(f"{config.IMAGE_SIZE} × {config.IMAGE_SIZE}")

    st.write("Classes")

    st.write(len(config.CLASS_NAMES))

# ----------------------------------------------------
# Upload
# ----------------------------------------------------

uploaded = st.file_uploader(

    "Upload PCB Image",

    type=["png","jpg","jpeg","bmp"]

)

# ----------------------------------------------------
# Stop if no image
# ----------------------------------------------------

if uploaded is None:

    st.info("Upload a PCB image to begin prediction.")

    st.stop()

# ----------------------------------------------------
# Load Image
# ----------------------------------------------------

image = Image.open(uploaded).convert("RGB")

draw = ImageDraw.Draw(image)

# ----------------------------------------------------
# Predict
# ----------------------------------------------------

result = predict_image(image)

prediction = result["prediction"]

confidence = result["confidence"]

# ----------------------------------------------------
# Draw Prediction
# ----------------------------------------------------

draw.rectangle(

    [(5,5),(260,60)],

    fill="black"

)

draw.text(

    (15,20),

    f"{prediction} ({confidence:.1f}%)",

    fill="white"

)

# ----------------------------------------------------
# Layout
# ----------------------------------------------------

left, right = st.columns([1.4, 1], gap="large")

with left:

    st.image(
    image,
    caption="Uploaded PCB Image",
    width=600
)

with right:

    prediction_card(result)

    st.markdown("<br>", unsafe_allow_html=True)

    metrics_row(result)

    st.markdown("<br>", unsafe_allow_html=True)

    if confidence < 70:

        st.warning(

            "⚠ Low confidence prediction.\n\nManual inspection is recommended."

        )

    else:

        st.success(

            "✅ High confidence prediction."

        )
    # ----------------------------------------------------
# Charts
# ----------------------------------------------------

st.divider()

c1, c2 = st.columns(2, gap="large")

with c1:
    st.plotly_chart(
        confidence_gauge(result["confidence"]),
        use_container_width=True
    )

with c2:
    st.plotly_chart(
        top3_chart(result["top3"]),
        use_container_width=True
    )

st.plotly_chart(
    probability_chart(
        config.CLASS_NAMES,
        result["probabilities"]
    ),
    use_container_width=True
)

# ----------------------------------------------------
# Download Report
# ----------------------------------------------------

st.divider()

st.subheader("📄 Prediction Report")

report = pd.DataFrame({

    "Prediction":[

        result["prediction"]

    ],

    "Confidence (%)":[

        round(result["confidence"],2)

    ],

    "Inference Time (ms)":[

        round(result["inference_time"],2)

    ]

})

st.dataframe(

    report,

    use_container_width=True,

    hide_index=True

)

csv = report.to_csv(

    index=False

).encode("utf-8")

st.download_button(

    label="⬇ Download Prediction Report",

    data=csv,

    file_name="prediction_report.csv",

    mime="text/csv"

)

# ----------------------------------------------------
# Top-3 Table
# ----------------------------------------------------

st.divider()

top3_table(result)

# ----------------------------------------------------
# Footer
# ----------------------------------------------------
st.divider()

a, b, c = st.columns(3, gap="large")

with a:
    model_card()

with b:
    device_card()

with c:
    st.success(
        """
### 🚀 Deployment Status

Ready for Edge AI Deployment

✔ ConvNeXt Tiny

✔ ONNX Compatible

✔ GPU Accelerated
"""
    )
footer()