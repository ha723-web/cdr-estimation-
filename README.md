
# 👁️ Cup-to-Disc Ratio Estimator for Glaucoma Detection

A medical AI application to assist in **early detection of glaucoma** by calculating the **Cup-to-Disc Ratio (CDR)** from retinal fundus images. Built using Python, OpenCV, and Streamlit.

---

## 📦 Project Setup & Execution (Mac + VS Code Compatible)

### ✅ Step-by-Step Terminal Commands

bash
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

✅ The app will open in your browser at: [http://localhost:8501](http://localhost:8501)

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

## 🧪 Example Terminal Session (Mac Setup)

```bash
Last login: Sat May 24 01:44:02 on console
harshiniakunuri@Mac ~ % cd ~/Desktop
harshiniakunuri@Mac Desktop % cd cdr-estimator
harshiniakunuri@Mac cdr-estimator % python3 -m venv venv
harshiniakunuri@Mac cdr-estimator % source venv/bin/activate
(venv) harshiniakunuri@Mac cdr-estimator % pip install -r requirements.txt
(venv) harshiniakunuri@Mac cdr-estimator % streamlit run app.py
```

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

