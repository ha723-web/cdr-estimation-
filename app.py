import streamlit as st
from detect_cup_disc import detect_cup_disc
from pdf_report import create_report
import cv2
import os

st.title("👁️ Cup-to-Disc Ratio Estimator")

uploaded = st.file_uploader("Upload a retinal image", type=['jpg', 'png'])

if uploaded:
    os.makedirs("output", exist_ok=True)
    file_path = os.path.join("output", uploaded.name)
    with open(file_path, "wb") as f:
        f.write(uploaded.read())

    processed_img, cdr = detect_cup_disc(file_path)

    st.image(processed_img, caption="Processed Image with Cup & Disc")

    if cdr:
        st.write(f"🔢 **CDR (Cup-to-Disc Ratio)**: `{cdr}`")
        if cdr > 0.6:
            st.error("⚠️ High CDR: Risk of Glaucoma!")
        else:
            st.success("✅ Normal CDR")

        result = "High Risk of Glaucoma" if cdr > 0.6 else "Normal"
        create_report(cdr, result, uploaded.name)
        st.download_button("📄 Download PDF Report", open("output/report.pdf", "rb"), file_name="glaucoma_report.pdf")
    else:
        st.warning("⚠️ Could not detect both cup and disc. Try another image.")

import matplotlib.pyplot as plt

# ⬇️ Replace this section in app.py (AFTER image processing is done)

# Create side-by-side plots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Show original image
axs[0].imshow(image_rgb)
axs[0].set_title("Original Retinal Image")
axs[0].axis('off')

# Show image with detected circles
axs[1].imshow(output_img_rgb)
axs[1].set_title(f"CDR: {cdr:.2f} — {'Normal' if cdr <= 0.6 else 'Risk of Glaucoma'}")
axs[1].axis('off')

# Display in Streamlit
st.pyplot(fig)
