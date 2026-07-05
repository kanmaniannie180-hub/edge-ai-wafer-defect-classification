# 🧪 PCB Defect Class Definitions

This document defines the **eight PCB defect classes** used for training and evaluating the **ConvNeXt Tiny PCB Defect Classification System**.

Each class is described based on its **visual characteristics** observed in PCB inspection images to ensure **consistent annotation, reproducibility, and reliable model training**.

> **Note:** The images shown below are provided **only as visual references** to illustrate each defect category. They are **not necessarily the exact images used for training, validation, or testing**.

---

# 1️⃣ Clean

### Description

Inspection images that show **normal PCB regions** without any visible manufacturing defects or structural abnormalities.

### Visual Characteristics

- Uniform copper traces
- No scratches or cracks
- No broken tracks
- No unwanted conductive connections
- Consistent spacing between traces

### Typical Impact

This class represents **defect-free PCB samples** and serves as the reference class for comparison.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/0bc0a1b2-e40f-41a9-8c8c-7a48331f3f36" />

---

# 2️⃣ Other

### Description

Images containing anomalies that do not clearly belong to one of the predefined PCB defect categories.

### Visual Characteristics

- Surface contamination
- Dust or particles
- Manufacturing residue
- Unknown or uncommon defects
- Irregular surface patterns

### Why this class exists

This category prevents ambiguous defects from being incorrectly assigned to other classes, improving the robustness of the classification model.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/d06facd8-64f3-4f06-b646-27ab316f2164" />

---

# 3️⃣ Short

### Description

Short defects occur when unintended conductive material creates an electrical connection between adjacent PCB traces.

### Visual Characteristics

- Narrow conductive bridges
- Reduced spacing between traces
- Excess copper connecting nearby tracks

### Typical Impact

Short circuits may cause incorrect signal transmission or complete circuit failure.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/3420313a-f578-4478-99e0-4286dc58b82a" />

---

# 4️⃣ Open

### Description

Open defects occur when conductive traces are interrupted, resulting in an incomplete electrical connection.

### Visual Characteristics

- Broken copper traces
- Missing conductive segments
- Visible gaps in tracks
- Interrupted electrical pathways

### Typical Impact

Open circuits prevent proper electrical current flow and may cause complete device malfunction.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/d70ef643-c395-4aae-aa70-2257a453d09c" />

---

# 5️⃣ Bridges

### Description

Bridge defects occur when excess conductive material forms an unintended structural connection between adjacent PCB features.

### Visual Characteristics

- Thick copper connections
- Material overflow
- Adjacent traces physically joined
- Large conductive bridges

### Typical Impact

Bridge defects often result in electrical shorts and manufacturing failures.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/96a21fd6-2f08-4ef0-b77b-28badde4a292" />

---

# 6️⃣ Scratches

### Description

Scratches are linear surface defects introduced during PCB manufacturing, handling, or assembly.

### Visual Characteristics

- Long thin surface marks
- Parallel scratch lines
- Abrasion of copper or substrate
- Surface damage without complete fracture

### Typical Impact

Severe scratches may expose conductive material or weaken PCB reliability.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/983c1a15-6926-495c-9133-6c4a439aeb5f" />

---

# 7️⃣ Cracks

### Description

Cracks are structural fractures caused by mechanical stress, thermal expansion, or manufacturing defects.

### Visual Characteristics

- Irregular fracture lines
- Broken conductive paths
- Sharp discontinuities
- Non-uniform crack patterns

### Typical Impact

Cracks reduce structural integrity and may interrupt electrical conductivity.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/2a2ca491-8ea3-49f6-bd20-409904bc7d48" />

---

# 8️⃣ Malformed Vias

### Description

Malformed vias are defects involving incomplete, damaged, or improperly formed vias connecting PCB layers.

### Visual Characteristics

- Missing vias
- Irregular via geometry
- Misaligned drilling
- Partially filled vias

### Typical Impact

Malformed vias can reduce electrical connectivity between PCB layers and negatively affect circuit performance.

**Example:**

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/27e37383-14a5-42b3-81d7-0e46e7e70f01" />

---

# 🖼️ Visual Reference Policy

The images shown in this document are included **solely for illustrative purposes** to demonstrate the visual appearance of each defect category.

These reference images:

- Help explain the characteristics of each defect type.
- May originate from publicly available educational or research resources.
- Are **not necessarily the exact images used** for model training or evaluation.

The ConvNeXt Tiny classification model is trained and evaluated using the curated dataset described in **dataset.md**.

---

# 📌 Annotation Guidelines

To maintain dataset consistency:

- Each image is assigned **exactly one defect class**.
- Images containing multiple dominant defects are excluded.
- Class labels are derived directly from the dataset folder structure.
- All training, validation, and testing images follow the same class definitions.

These guidelines ensure reproducible experiments and consistent model evaluation.
