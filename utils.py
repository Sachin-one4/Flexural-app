import os
import tempfile
from fpdf import FPDF

def create_pdf(prediction, input_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Prediction Report", ln=True, align='C')

    # Example content
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Prediction: {prediction}", ln=True)

    pdf.ln(10)
    for key, value in input_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "prediction_report.pdf")
    pdf.output(file_path)
    return file_path
