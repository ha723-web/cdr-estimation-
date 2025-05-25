import streamlit as st
from detect_cup_disc import detect_cup_disc
from pdf_report import create_report
import cv2
import os
import matplotlib.pyplot as plt

st.title("👁️ Cup-to-Disc Ratio Estimator")

uploaded = st.file_uploader("Upload a retinal image", type=['jpg', 'png'])

if uploaded:
    os.makedirs("output", exist_ok=True)
    file_path = os.path.join("output", uploaded.name)
    with open(file_path, "wb") as f:
        f.write(uploaded.read())

    # ✅ Load original image
    image = cv2.imread(file_path)

    # ✅ Run detection
    output_img, cup_radius, disc_radius = detect_cup_disc(image)
    cdr = round(cup_radius / disc_radius, 2)

    # ✅ Convert for matplotlib visualization
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_img_rgb = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

    # ✅ Matplotlib side-by-side plot
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(image_rgb)
    axs[0].set_title("Original Retinal Image")
    axs[0].axis('off')

    axs[1].imshow(output_img_rgb)
    axs[1].set_title(f"CDR: {cdr:.2f} — {'Normal' if cdr <= 0.6 else 'Risk of Glaucoma'}")
    axs[1].axis('off')

    # ✅ Show in Streamlit
    st.pyplot(fig)

    # ✅ Display CDR and Classification
    st.write(f"🔢 **CDR (Cup-to-Disc Ratio)**: `{cdr}`")
    if cdr > 0.6:
        st.error("⚠️ High CDR: Risk of Glaucoma!")
    else:
        st.success("✅ Normal CDR")

    # ✅ Generate and allow download of report
    result = "High Risk of Glaucoma" if cdr > 0.6 else "Normal"
    create_report(cdr, result, uploaded.name)
    st.download_button("📄 Download PDF Report", open("output/report.pdf", "rb"), file_name="glaucoma_report.pdf")
