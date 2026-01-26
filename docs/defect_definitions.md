# 🧪 Defect Class Definitions (Phase-1)

This document defines the **defect classes** used in the **Phase-1 wafer/die inspection defect classification task**.

Each class is defined based on **visual characteristics observable in optical or SEM inspection images**. The goal is to ensure **label clarity, consistency, and reproducibility** across the dataset.

> **Note:** Organizer-provided sample images are used **only for visual reference**. They are **not included** in training, validation, or evaluation datasets.

---

## 1️⃣ Clean

### Description

Inspection images that show **nominal wafer or die patterns** with **no visible structural or surface anomalies**.

### Visual Characteristics

* Continuous and uniform patterns
* No breaks, bridges, scratches, or surface damage
* Consistent line width and spacing

### Notes

This class represents **defect-free samples** and serves as a **baseline reference** for defect comparison.

**Example:**
*(Insert one representative clean inspection image)*

---

## 2️⃣ Other

### Description

Images containing **anomalies that do not clearly belong** to any predefined defect category.

### Visual Characteristics

* Particles or contamination
* Surface residue or stains
* Edge roughness or irregular texture
* Unclassified or rare defect patterns

### Notes

This class prevents **forced mislabeling of ambiguous defects** and improves overall **model robustness**.

**Example:**
*(Insert one representative “other” defect image)*

---

## 3️⃣ Shorts

### Description

Defects where **unintended electrical connections** form between adjacent conductive lines or structures.

### Visual Characteristics

* Unintended material connecting neighboring lines
* Reduced spacing between features
* Localized conductive bridges

### Notes

Shorts typically originate from **process variations** or **material over-deposition**.

**Example:**
*(Insert one representative shorts defect image)*

---

## 4️⃣ Opens

### Description

Defects characterized by **broken or interrupted conductive paths**.

### Visual Characteristics

* Visible gaps in lines or interconnects
* Discontinuity in otherwise continuous patterns
* Missing material segments

### Notes

Opens result in **electrical discontinuity** and can cause **functional failure**.

**Example:**
*(Insert one representative opens defect image)*

---

## 5️⃣ Bridges

### Description

Defects where **two or more structures are unintentionally connected** due to excess material.

### Visual Characteristics

* Thickened regions connecting adjacent features
* Material spillover between lines
* Clear structural linkage between separate patterns

### Notes

Bridges are **visually distinct from shorts** due to **larger and more pronounced connecting regions**.

**Example:**
*(Insert one representative bridges defect image)*

---

## 6️⃣ CMP Scratches

### Description

Surface defects introduced during **Chemical Mechanical Planarization (CMP)** processes.

### Visual Characteristics

* Long, linear surface marks
* Parallel or gently curved scratch patterns
* Surface-level abrasions

### Notes

CMP scratches primarily affect **surface quality** and are commonly observed in **SEM images**.

**Example:**
*(Insert one representative CMP scratch image)*

---

## 7️⃣ Cracks

### Description

Structural fractures or breaks caused by **mechanical or thermal stress**.

### Visual Characteristics

* Jagged or irregular fracture lines
* Sharp edges and discontinuities
* Non-uniform thickness along the defect

### Notes

Cracks are **distinct from scratches** due to their **fractured, structural appearance**.

**Example:**
*(Insert one representative crack defect image)*

---

## 8️⃣ Malformed Vias

### Description

Defects involving **incomplete, missing, or deformed via structures**.

### Visual Characteristics

* Irregular via shapes
* Missing or partially filled vias
* Misaligned or collapsed via structures

### Notes

These defects are typically identified in **high-magnification inspection images**.

**Example:**
*(Insert one representative malformed via image)*

---

## 🔒 Class Finalization Statement

The above **eight defect classes are fixed for Phase-1** and **will not be modified**.

* Each image in the dataset is labeled with **exactly one dominant defect class**
* No multi-label or ambiguous annotations are allowed in Phase-1

This strict class definition ensures **dataset consistency**, **training stability**, and **fair evaluation**.
