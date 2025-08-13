# app.py
from utils import create_pdf
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64
import os
import tempfile
from fpdf import FPDF

# Example Home.py
import streamlit as st

def main():
    st.title("Welcome to the Flexural Strength App")
    st.write("This is the Home page.")


# Load model
model = joblib.load("model_pipeline.pkl")

# PDF Generation

def create_pdf(prediction, input_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Flexural Strength Prediction Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Prediction: {prediction}", ln=True)
    pdf.ln(5)

    for key, value in input_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "prediction_report.pdf")
    pdf.output(file_path)

    return file_path


def get_pdf_download_link(file_path):
    with open(file_path, "rb") as f:
        pdf_base64 = base64.b64encode(f.read()).decode("utf-8")
    return f'<a href="data:application/octet-stream;base64,{pdf_base64}" download="prediction_report.pdf">📄 Download PDF Report</a>'

# Streamlit UI
# st.set_page_config(page_title="Flexural Strength Predictor", layout="centered")
st.title("🔬 Flexural Strength Predictor")
st.markdown("A 6th SEM BTech Project using Machine Learning")

# Form
with st.form("prediction_form"):
    infill_density = st.number_input("Infill Density (%)", min_value=0, max_value=100, step=1)
    layer_height = st.number_input("Layer Height (mm)", min_value=0.05, max_value=1.0, step=0.01)
    nozzle_temp = st.number_input("Nozzle Temperature (°C)", min_value=150, max_value=300, step=1)
    pattern = st.selectbox("Pattern", ["Rectilinear", "Honeycomb", "Gyroid"])
    submit = st.form_submit_button("🔍 Predict")

if submit:
    input_data = pd.DataFrame({
        "Infill Density": [infill_density],
        "Layer Height": [layer_height],
        "Nozzle Temp": [nozzle_temp],
        "Pattern": [pattern]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Predicted Flexural Strength: **{prediction:.2f}**")

    # Chart
    st.subheader("📊 Input Overview")
    fig, ax = plt.subplots()
    ax.bar(["Infill Density", "Layer Height", "Nozzle Temp"], [infill_density, layer_height, nozzle_temp], color='skyblue')
    ax.set_ylabel("Value")
    st.pyplot(fig)

    # PDF
    file_path = create_pdf(prediction, input_data)
    st.markdown(get_pdf_download_link(file_path), unsafe_allow_html=True)

# Bulk Prediction
# st.markdown("---")
# st.subheader("📁 Upload CSV for Bulk Prediction")
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     try:
#         preds = model.predict(df)
#         df["Predicted Flexural Strength"] = preds
#         st.success("Predictions complete!")
#         st.dataframe(df)

#         csv = df.to_csv(index=False).encode("utf-8")
#         st.download_button("⬇️ Download Results CSV", data=csv, file_name="predictions.csv", mime="text/csv")
#     except Exception as e:
#         st.error(f"Error: {e}")

# About Us
st.markdown("---")
st.subheader("👨‍💻 About the Team")
st.markdown("Meet the developers behind this final-year BTech project.")

# Define team members
team = [
    {
        "name": "SACHIN",
        "roll": "23001020505",
        "role": "Model Training & Evaluation",
        "image": "self.jpg"
    },
    {
        "name": "NAMAN",
        "roll": "23001020504",
        "role": "Report writing and frontend",
        "image": "naman.jpg"  # Replace with real file if available
    },
    {
        "name": "MOHD SAIF ALI",
        "roll": "23001020503",
        "role": "Frontend & Data Preprocessing",
        "image": "saif.jpg"  # Replace with real file if available
    }
]

# Display team members
cols = st.columns(3)
for i, member in enumerate(team):
    with cols[i]:
        st.image(member["image"], width=150)
        st.markdown(f"**{member['name']}**")
        st.markdown(f"Roll No: {member['roll']}")
        st.markdown(f"Role: *{member['role']}*")
