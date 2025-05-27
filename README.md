
# 👁️ Cup-to-Disc Ratio Estimator for Glaucoma Detection

A medical AI application to assist in **early detection of glaucoma** by calculating the **Cup-to-Disc Ratio (CDR)** from retinal fundus images. Built using Python, OpenCV, and Streamlit.

liNK TO THE APP - https://glaucoma-cdr-checker.streamlit.app/
---

## 🧠 What I Learned Through This Project

### 👁️ 1. Anatomy of the Eye (Basic Ophthalmology)

* The **retina** is the light-sensitive layer at the back of the eye.
* The **optic disc** is the entry point of the optic nerve — it appears as a circular white region.
* The **optic cup** is a small depression within the optic disc.
* The **Cup-to-Disc Ratio (CDR)** is the ratio of the cup diameter to the disc diameter.
  A **larger cup** may signal damage to the optic nerve — often a sign of **glaucoma**.

### ⚠️ 2. Understanding Glaucoma

* Glaucoma is a serious condition that can cause **permanent vision loss** if not caught early.
* **Elevated CDR values** (typically above 0.6) are a red flag for possible glaucoma.
* Manual diagnosis through fundus imaging requires expertise — this motivated an automated approach.

---

## 🤖 3. Applying AI & Computer Vision

### 🔍 OpenCV Techniques

* Used **Hough Circle Transform** to detect circular features (optic disc & cup) in fundus images.
* Applied **grayscale conversion**, **blurring**, and **thresholding** to enhance feature detection.
* Calculated CDR by sorting detected circles by radius and dividing their sizes.

---

## 🧮 4. CDR Calculation Logic

* Once circles are detected:

  ```
  CDR = Radius of Cup / Radius of Disc
  ```
* If CDR > 0.6 → Show warning
* If CDR ≤ 0.6 → Show normal result

The image is also **visually marked with both circles** using OpenCV’s drawing functions.

---

## 🌐 5. Interactive Streamlit Web App

* Designed a clean **web interface** using Streamlit where:

  * Users can upload fundus images
  * View the CDR result and classification
  * **Download a PDF report** summarizing the analysis
* Implemented **Streamlit components** such as `file_uploader`, `image`, `markdown`, and `download_button`.

---

## 📄 6. Report Generation

* Used **FPDF library** to auto-generate a diagnostic report.
* Report includes:

  * Filename
  * CDR value
  * Classification (Normal/Risk)
  * Timestamp

---

## 💡 Final Takeaways

* Gained a **strong understanding of medical imaging** through a real-world eye disease use case.
* Learned to **bridge healthcare knowledge with AI tools**.
* Built a full-stack app combining **OpenCV, Python, Streamlit, and PDF generation**.
* Practiced **debugging virtual environments on Mac (PEP 668)** and GitHub project documentation.

---

## 🗂️ Files & Folder Structure

```
cdr-estimator/
├── app.py               # Streamlit app logic
├── detect_cup_disc.py   # Image processing with OpenCV
├── pdf_report.py        # PDF generation logic
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── retina_images/       # (Add test images here)
└── output/              # Processed images and reports
```

---

## 🧠 What the App Does

* 📤 Upload a **retinal fundus image**
* 🔍 Detect **optic cup** and **optic disc** using Hough Circle detection (OpenCV)
* 🧮 Calculate **Cup-to-Disc Ratio (CDR = cup / disc)**
* 🩺 Classify based on CDR:

  * ✅ **Normal** if CDR ≤ 0.6
  * ⚠️ **Risk of Glaucoma** if CDR > 0.6
* 📄 Downloadable **PDF report** with results

---

## 📦 Project Setup & Execution (Mac + VS Code Compatible)

### ✅ Step-by-Step Terminal Commands
```bash

cd ~/Desktop
cd cdr-estimator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
✅ The app will open in your browser at: [http://localhost:8501](http://localhost:8501)

---

## ⚠️ Disclaimer

This tool is built purely for **learning, analysis, and curiosity**.
It is **not a certified medical tool** and should not be used for real diagnostic decisions.
Always consult a licensed ophthalmologist for medical advice.
The author is not responsible for any use or misuse of this tool.

---

## 👩‍⚕️ Author

**Harshini Akunuri**
M.S. in Computer Science | Passionate about AI in Healthcare
📫 [harshiniakunuri59@gmail.com](mailto:harshiniakunuri59@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/harshini-akunuri)

