"""
=========================================================
UI Components
PCB Defect Streamlit Dashboard
=========================================================
"""

import streamlit as st

from utils import (
    percent,
    get_emoji,
    badge_color,
    get_device_information
)

# -------------------------------------------------------
# Header
# -------------------------------------------------------

def page_header():

    st.markdown(
        """
        # 🔍 PCB Defect Classification Dashboard
        ### ConvNeXt Tiny • Transfer Learning • PyTorch
        """
    )

    st.divider()


# -------------------------------------------------------
# Prediction Card
# -------------------------------------------------------

# -------------------------------------------------------
# Prediction Card
# -------------------------------------------------------

def prediction_card(result):

    confidence = result["confidence"]

    prediction = result["prediction"]

    color = badge_color(confidence)

    emoji = get_emoji(prediction)

    # Confidence Level
    if confidence >= 90:
        level = "🟢 High Confidence"
        message = "Prediction is highly reliable."

    elif confidence >= 70:
        level = "🟡 Medium Confidence"
        message = "Prediction is reasonably reliable."

    else:
        level = "🔴 Low Confidence"
        message = "Model is uncertain. Manual inspection is recommended."

    st.markdown(
        f"""
        <div style="
            border-left:8px solid {color};
            padding:22px;
            border-radius:15px;
            background:#1b1f27;
            box-shadow:0px 5px 15px rgba(0,0,0,0.12);
        ">

        <h2>{emoji} {prediction.replace('_',' ').title()}</h2>
        <h2 style="color:white;">
        <h3 style="color:{color}; margin-bottom:5px;">
            {confidence:.2f}%
        </h3>

        <h4>{level}</h4>

        <p style="font-size:16px;color:#d1d5db;">
            {message}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------------
# Metrics
# -------------------------------------------------------

def metrics_row(result):

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Confidence",

            percent(result["confidence"])

        )

    with c2:

        st.metric(

            "Inference",

            f"{result['inference_time']:.2f} ms"

        )

    with c3:

        st.metric(

            "Prediction",

            result["prediction"]

        )


# -------------------------------------------------------
# Device Card
# -------------------------------------------------------

def device_card():

    info = get_device_information()

    st.subheader("💻 System")

    st.info(

f"""
**Device**

{info['device']}

**GPU**

{info['gpu']}

**CUDA**

{info['cuda']}

**Memory**

{info['memory']} GB
"""

    )


# -------------------------------------------------------
# Model Card
# -------------------------------------------------------

def model_card():

    st.subheader("🧠 Model")

    st.success(

"""
Architecture

ConvNeXt Tiny

Transfer Learning

ImageNet Pretrained

Input Size

224 × 224

Classes

8

Framework

PyTorch
"""

    )


# -------------------------------------------------------
# Top-3 Predictions
# -------------------------------------------------------

def top3_table(result):

    st.subheader("🏆 Top 3 Predictions")

    medals = ["🥇", "🥈", "🥉"]

    for medal, (cls, prob) in zip(

        medals,

        result["top3"]

    ):

        st.write(

            f"{medal} **{cls.replace('_',' ').title()}** — {prob*100:.2f}%"

        )


# -------------------------------------------------------
# Footer
# -------------------------------------------------------

def footer():

    st.divider()

    st.caption(

        "PCB Defect Classification Dashboard | "
        "ConvNeXt Tiny | PyTorch | Streamlit"

    )