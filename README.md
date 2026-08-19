# AI-Powered Plant Disease Detection

Hey everyone! Welcome to my AI-powered plant disease detection project. I built this app to make it easy for gardeners, students, and farmers to take a picture of a plant leaf and instantly figure out what disease it might have, how severe it is, and what they can do to fix it.

I used a deep learning model built with TensorFlow/Keras and wrapped it in a clean, interactive web app using Streamlit. 

---

## Application Screenshots

Here is a quick look at the web application interface and prediction results:

### Home View / Upload Interface
![App Interface](so1.png)

### Prediction & Recommendation Results
![App Results](so2.png)

---

## What It Can Do
* **Instant Image Upload:** Upload any clear photo of a plant leaf (JPG, PNG).
* **AI Predictions:** Uses a fine-tuned MobileNetV2 architecture to recognize plant conditions and display a confidence score.
* **Actionable Advice:** Pulls up a custom database containing detailed symptoms, prevention tips, and treatment options for each condition.
* **Clean UI:** Built with Streamlit for a smooth, fast local web interface.

---

## Project Structure
Here is how the project files are organized:
```text
AI-Powered-Plant-Disease-Detection/
│
├── data/                  # Dataset references / info
├── models/
│   └── plant_model_weights.weights.h5   # Trained model weights
├── notebooks/
│   └── plant_disease_training.ipynb     # Training notebook (Colab)
├── src/
│   ├── __init__.py
│   ├── predict.py         # Model loading & inference logic
│   ├── preprocess.py      # Image resizing & normalization
│   └── disease_info.py    # Symptoms & treatment database
│
├── class_indices.json     # Class name mappings
├── app.py                 # Main Streamlit web application
├── requirements.txt       # Project dependencies
├── so1.png                # App screenshot 1
├── so2.png                # App screenshot 2
└── README.md
