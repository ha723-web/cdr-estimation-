# 👁️ Cup-to-Disc Ratio Estimator for Glaucoma Detection

A medical AI application to assist in **early detection of glaucoma** by calculating the **Cup-to-Disc Ratio (CDR)** from retinal fundus images. Built using Python, OpenCV, and Streamlit.

---

## 📦 Project Setup & Execution (Mac + VS Code Compatible)

### ✅ Step-by-Step Terminal Commands

```bash
# 1. Navigate to Desktop where project folder is located
cd ~/Desktop

# 2. Enter your project folder
cd cdr-estimator

# 3. Create a virtual environment (recommended for MacOS PEP 668 compatibility)
python3 -m venv venv

# 4. Activate the virtual environment
source venv/bin/activate

# 5. Install required Python libraries
pip install -r requirements.txt

# 6. Run the Streamlit app
streamlit run app.py


# 👁️ Cup-to-Disc Ratio Estimator for Glaucoma Detection

This project helps in early screening of glaucoma by estimating the **Cup-to-Disc Ratio (CDR)** from retinal fundus images. It's built using Python, OpenCV, and Streamlit, and includes real-time image analysis with a downloadable PDF report.

---

## ⚙️ Files & Folder Structure

cdr-estimator/
├── app.py # Streamlit app logic
├── detect_cup_disc.py # Image processing with OpenCV
├── pdf_report.py # PDF generation logic
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── retina_images/ # (Add test images here)
└── output/ # Processed images and reports


---

## 🧠 What the App Does

- 📤 Upload a retinal fundus image
- 🧠 Detect **optic cup** and **optic disc** using Hough Circle detection (OpenCV)
- 🧮 Calculate **Cup-to-Disc Ratio (CDR = cup / disc)**
- 📊 Classify based on CDR:
  - ✅ **Normal** if CDR ≤ 0.6
  - ⚠️ **Risk of Glaucoma** if CDR > 0.6
- 📄 Downloadable **PDF report** with results

---

## 🧪 Example Terminal Session (Mac Setup)

```bash
# 1. Go to Desktop
cd ~/Desktop

# 2. Navigate into project folder
cd cdr-estimator

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate virtual environment
source venv/bin/activate

# 5. Install project dependencies
pip install -r requirements.txt

# 6. Launch the app
streamlit run app.py

✅ The app will open at: http://localhost:8501

---

👩‍⚕️ Author
Harshini Akunuri
M.S. Computer Science | Passionate about AI in Healthcare
📫 harshiniakunuri59@gmail.com
🔗 LinkedIn

---
---

## ⚠️ Disclaimer

This project is developed purely for **educational, experimental, and personal learning purposes**.  
It is **not** a certified medical tool or diagnostic system.

The Cup-to-Disc Ratio (CDR) analysis is a **basic computer vision-based prediction**, intended to simulate how AI might be used in ophthalmology. The predictions are **not validated by clinical experts**, and the results **should not be used to make medical decisions**.

The developer assumes **no responsibility for any harm, direct or indirect**, caused by the use or misuse of this software.

If you're concerned about your eye health, please consult a **licensed ophthalmologist**.



