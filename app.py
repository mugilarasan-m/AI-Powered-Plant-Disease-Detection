import streamlit as st
from PIL import Image
import os

from src.preprocess import prepare_image
from src.predict import predict_plant_disease, model
from src.disease_info import get_disease_details

st.set_page_config(
    page_title="AI Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 AI-Powered Plant Disease Detection")
st.markdown("""
Welcome to the Plant Disease Detection system! Upload a clear photo of a plant leaf below,
and our AI model will analyze it to detect potential diseases, assess confidence, and provide recommendations.
""")

st.markdown("---")

uploaded_file = st.file_uploader(
    "Choose a plant leaf image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Image")
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)

    with col2:
        if model is None:
            st.error(
                "Model could not be loaded. Please check your model weights file."
            )
        else:
            if st.button("🔍 Predict Plant Condition", type="primary"):
                with st.spinner("Analyzing image... Please wait..."):
                    try:
                        processed_img = prepare_image(uploaded_file)

                        class_name, confidence = predict_plant_disease(processed_img)

                        details = get_disease_details(class_name)

                        st.markdown("---")
                        st.subheader("📊 Analysis Results")

                        st.metric(
                            "Predicted Condition",
                            details["disease"]
                        )

                        st.metric(
                            "Confidence Score",
                            f"{confidence * 100:.2f}%"
                        )

                        st.markdown(
                            f"**Plant Type:** {details['plant']}"
                        )

                        st.markdown("### 📋 Disease Information")
                        st.info(details["description"])

                        st.markdown("### ⚠️ Symptoms")
                        st.write(details["symptoms"])

                        st.markdown("### 🛡️ Prevention Methods")
                        st.success(details["prevention"])

                        st.markdown("### 💊 Treatment Recommendations")
                        st.warning(details["treatment"])

                        st.markdown("""
                        ---
                        *Disclaimer: Recommendations are provided for educational purposes only.
                        Please consult a local agricultural extension office or expert for severe infections.*
                        """)

                    except Exception as e:
                        st.error(
                            f"An error occurred during prediction: {e}"
                        )

else:
    st.info(
        "👆 Please upload an image file (JPG, JPEG, or PNG) to get started."
    )