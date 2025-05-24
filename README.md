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


Absolutely, Harshini! Here's your updated `README.md` structure with **bold, clear section headers** using your requested format and styling — exactly like the GitHub style you're aiming for.

---

```markdown

Thanks, Harshini! I see the issue — GitHub markdown does **not support bold headers** when using both `##` and `**bold**` together. That’s why the format looks off in the preview.

To get the clean, bold **section headers** you want, just use **`#` or `##` without extra asterisks**, and use **emojis for visual styling**.

---

## ✅ Final Fix – Use This Format

```markdown
# 👁️ Cup-to-Disc Ratio Estimator for Glaucoma Detection

A medical AI application to assist in **early detection of glaucoma** by calculating the **Cup-to-Disc Ratio (CDR)** from retinal fundus images.

---

## 🗂️ Files & Folder Structure

```

cdr-estimator/
├── app.py               # Streamlit app logic
├── detect\_cup\_disc.py   # Image processing with OpenCV
├── pdf\_report.py        # PDF generation logic
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── retina\_images/       # (Add test images here)
└── output/              # Processed images and reports

````

---

## 🧠 What the App Does

- 📤 Upload a **retinal fundus image**
- 🔍 Detect **optic cup** and **optic disc** using Hough Circle detection (OpenCV)
- 🧮 Calculate **Cup-to-Disc Ratio (CDR = cup / disc)**
- 🩺 Classify based on CDR:
  - ✅ Normal if CDR ≤ 0.6
  - ⚠️ Risk of Glaucoma if CDR > 0.6
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

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run the app
streamlit run app.py
````

✅ The app will open in your browser at: [http://localhost:8501](http://localhost:8501)

---

## ⚠️ Disclaimer

This tool is built for **learning, analysis, and curiosity only**.
It is **not a diagnostic tool** and should never be used for medical decisions.

---

## 👩‍⚕️ Author

**Harshini Akunuri**
M.S. in Computer Science | Passionate about AI in Healthcare
📫 [harshiniakunuri59@gmail.com](mailto:harshiniakunuri59@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/harshini-akunuri)

```

---






