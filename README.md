# 🌿 AgriVision AI: Crop Disease Detection & Precision Agronomy

An end-to-end intelligent computer vision web application for crop disease identification and agronomic advisory. Built with **MobileNetV2 CNN architecture**, trained on the benchmark **PlantVillage dataset from Kaggle**, powered by a **Flask** backend with **SQLite database**, **User ID generation & authentication**, and a **stored dataset visual comparison engine**.

---

## 🚀 Key Features

1. **Exact Leaf Disease Identification**:
   - Classifies 38 distinct plant conditions across 14 vital agricultural crops (Tomato, Potato, Apple, Corn, Grape, Bell Pepper, Peach, Cherry, Strawberry, Orange, Squash, Soybean, Blueberry, Raspberry).
   - Generates exact disease names, scientific pathogen nomenclature, severity index, and Top-3 softmax confidence probabilities.

2. **Stored Dataset Comparison Engine**:
   - Directly compares the user's uploaded leaf against stored ground-truth reference samples from the PlantVillage dataset.
   - Dual-view visual comparison: Uploaded Leaf vs. Stored Dataset Reference vs. Healthy Baseline leaf of the same crop.
   - Calculates a quantitative visual similarity match index (%) utilizing HSV Color Histogram correlation and structural pattern similarity.

3. **Precision Fertilizer & Nutrient Recommendations**:
   - Primary N-P-K ratios tailored to each disease condition.
   - Crucial micronutrients (Calcium, Potassium, Zinc, Magnesium, Silicon) to fortify cell walls and boost systemic resistance.
   - Application timing, dosage, and soil pH targets.
   - Clear warnings on fertilizers to strictly avoid during active infection (e.g. excessive nitrogen).

4. **Cultural Precautions & Sanitation**:
   - Drip vs. overhead irrigation guidelines to eliminate prolonged leaf wetness.
   - Pruning hygiene and 70% alcohol tool sanitization.
   - Plant spacing for canopy ventilation and crop rotation cycles (3+ years).

5. **Dual Treatment Action Plans**:
   - **Chemical Controls**: Active fungicides/bactericides with dosage, application timing, and pre-harvest intervals.
   - **Organic / Biological Remedies**: Neem oil, *Bacillus subtilis*, *Trichoderma*, and potassium bicarbonate.
   - **3-Phase Recovery Roadmap**: Days 1–3 (Emergency), Days 4–10 (Suppression), Days 14+ (Maintenance).

6. **Farmer Authentication & Unique User ID Creation**:
   - Generates a unique identifier (e.g., `AGRI-USER-74921`).
   - Secure password hashing using PBKDF2 with SHA-256 (`werkzeug.security`).
   - Profile management with farm location and primary crops grown.
   - Personal diagnosis history logs with printable official reports.

7. **Dataset Explorer & Comparison Studio**:
   - Browse all 38 PlantVillage classes with sample leaf photos, symptoms, and treatment plans.
   - Compare any custom leaf against any dataset benchmark.

---

## 📂 Project Architecture

```
Crop Disease/
├── app.py                     # Main Flask web application & API routing
├── config.py                  # System configuration (paths, security, thresholds)
├── database.py                # SQLite ORM & authentication (User ID, Diagnoses logs)
├── disease_data.py            # Agronomic knowledge base (38 classes, fertilizers, precautions)
├── model_loader.py            # MobileNetV2 inference engine & dataset comparison algorithm
├── train_mobilenetv2.py       # Standalone MobileNetV2 training & fine-tuning script
├── requirements.txt           # Python library dependencies
├── README.md                  # Complete project documentation
├── models/
│   └── crop_disease_model.h5  # Trained MobileNetV2 CNN weights
├── static/
│   ├── css/custom.css         # Styling, glassmorphism, and responsive layout
│   ├── js/main.js             # Drag-and-drop upload, image preview, animations
│   ├── uploads/               # User-uploaded leaf scans
│   └── dataset_samples/       # Stored representative reference images (38 classes)
└── templates/
    ├── base.html              # Base HTML template with navbar and session controls
    ├── index.html             # Main dashboard & drag-and-drop leaf uploader
    ├── result.html            # Detailed diagnosis report & side-by-side dataset comparison
    ├── compare.html           # Interactive benchmark comparison studio
    ├── library.html           # 38-class PlantVillage dataset encyclopedia
    ├── history.html           # Personal scan logbook & past reports
    ├── profile.html           # Digital Farmer ID card & account overview
    ├── login.html             # User login form (User ID / Username / Email)
    ├── register.html          # Registration form with unique User ID assignment
    └── analytics.html         # Visual farm health & disease telemetry charts
```

---

## 🧠 Model Architecture: MobileNetV2

- **Base Architecture**: Pre-trained `MobileNetV2` featuring Inverted Residual Blocks and Linear Bottlenecks.
- **Input Dimensions**: `(224, 224, 3)` normalized to `[0.0, 1.0]`.
- **Top Layers**:
  - `GlobalAveragePooling2D`
  - `Dense(256, activation='relu')`
  - `BatchNormalization`
  - `Dropout(0.4)`
  - `Dense(38, activation='softmax')`
- **Output**: Multi-class probability distribution across all 38 PlantVillage categories.

---

## 🛠️ Installation & Setup Guide

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your system.

### 2. Install Required Dependencies
Open PowerShell or Terminal in the project root directory and execute:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Web Application
```bash
python app.py
```
By default, the server starts at:
```
http://127.0.0.1:5000/
```

### 4. Create Your Account & Farmer User ID
1. Navigate to `http://127.0.0.1:5000/register`.
2. Enter your Name, Username, Email, Password, and Farm Location.
3. The system generates your unique **Farmer ID** (e.g. `AGRI-USER-XXXXX`).
4. Sign in with either your Username or your newly assigned User ID.

### 5. Diagnose a Crop Leaf
1. On the dashboard, drag and drop an image of an affected leaf or click to browse.
2. Click **Diagnose Disease & Compare Dataset Reference**.
3. Review:
   - Exact Disease Name & Pathogen identification.
   - Side-by-side visual comparison with stored PlantVillage ground-truth reference leaf.
   - Quantitative similarity score (%).
   - Precision Fertilizer formulations (NPK, Calcium, Potassium, Micronutrients).
   - Immediate cultural precautions and sanitation measures.
   - Chemical fungicides and organic bio-control options.
   - Click **Print Official Report** to save or print a PDF summary.

---

## 🔬 Training MobileNetV2 on Custom Datasets
To train or fine-tune MobileNetV2 on an external dataset:
```bash
python train_mobilenetv2.py --dataset "path/to/PlantVillage/train" --output "models/crop_disease_model.h5" --epochs 15 --batch_size 32
```
