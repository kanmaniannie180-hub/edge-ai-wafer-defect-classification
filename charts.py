"""
=========================================================
Charts
PCB Defect Streamlit Dashboard
=========================================================
"""

from __future__ import annotations

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# -------------------------------------------------------
# Confidence Gauge
# -------------------------------------------------------

def confidence_gauge(confidence):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=confidence,

        number={
            "suffix":"%"
        },

        title={
            "text":"Confidence"
        },

        gauge={

            "axis":{

                "range":[0,100]

            },

            "bar":{

                "color":"royalblue"

            },

            "steps":[

                {
                    "range":[0,40],
                    "color":"#ff4d4d"
                },

                {
                    "range":[40,70],
                    "color":"#ffd633"
                },

                {
                    "range":[70,90],
                    "color":"#66cc66"
                },

                {
                    "range":[90,100],
                    "color":"#00b300"
                }

            ]

        }

    ))

    fig.update_layout(

        height=320,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )

    )

    return fig


# -------------------------------------------------------
# Probability Bar Chart
# -------------------------------------------------------

def probability_chart(class_names, probabilities):

    df = pd.DataFrame({

        "Class":class_names,

        "Probability":probabilities*100

    })

    df = df.sort_values(

        by="Probability",

        ascending=True

    )

    fig = px.bar(

        df,

        x="Probability",

        y="Class",

        orientation="h",

        text="Probability"

    )

    fig.update_traces(

        texttemplate="%{text:.2f}%",

        textposition="outside"

    )

    fig.update_layout(

        title="Prediction Probabilities",

        xaxis_title="Confidence (%)",

        yaxis_title="",

        height=500,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    return fig


# -------------------------------------------------------
# Top-3 Predictions
# -------------------------------------------------------

def top3_chart(top3):

    classes = [x[0] for x in top3]

    scores = [x[1]*100 for x in top3]

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=classes,

            y=scores,

            text=[

                f"{x:.2f}%"

                for x in scores

            ],

            textposition="outside"

        )

    )

    fig.update_layout(

        title="Top 3 Predictions",

        xaxis_title="",

        yaxis_title="Confidence (%)",

        height=380,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    return fig