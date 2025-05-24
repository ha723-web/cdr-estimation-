from fpdf import FPDF

def create_report(cdr, result, image_name, output_path="output/report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="Glaucoma Detection Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Image: {image_name}", ln=True)
    pdf.cell(200, 10, txt=f"Cup-to-Disc Ratio (CDR): {cdr}", ln=True)
    pdf.cell(200, 10, txt=f"Diagnosis: {result}", ln=True)

    pdf.output(output_path)
