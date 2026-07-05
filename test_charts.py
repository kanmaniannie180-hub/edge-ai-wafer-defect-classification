from charts import *

classes = [

    "bridges",
    "clean",
    "cracks",
    "malformed_vias",
    "open",
    "other",
    "scratches",
    "short"

]

import numpy as np

probs = np.array([

    0.01,
    0.04,
    0.81,
    0.02,
    0.03,
    0.04,
    0.03,
    0.02

])

top3 = [

    ("cracks",0.81),

    ("clean",0.04),

    ("other",0.04)

]

confidence_gauge(81).show()

probability_chart(classes,probs).show()

top3_chart(top3).show()