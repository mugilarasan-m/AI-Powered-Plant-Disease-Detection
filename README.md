Here is your updated `README.md` file formatted cleanly and saved without any icons or emojis:

# AI-Powered Plant Disease Detection

Hey everyone! Welcome to my AI-powered plant disease detection project. I built this app to make it easy for gardeners, students, and farmers to take a picture of a plant leaf and instantly figure out what disease it might have, how severe it is, and what they can do to fix it.

I used a deep learning model built with TensorFlow/Keras and wrapped it in a clean, interactive web app using Streamlit. 

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
└── README.md

```

---

## How to Run It Locally

If you want to run this app on your own machine, follow these simple steps:

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR-USERNAME/AI-Powered-Plant-Disease-Detection.git](https://github.com/YOUR-USERNAME/AI-Powered-Plant-Disease-Detection.git)
cd AI-Powered-Plant-Disease-Detection

```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Launch the Streamlit App

```bash
streamlit run app.py

```

This will automatically open up the web app in your default browser at `http://localhost:8501`.

---

## How It Works Behind the Scenes

1. **Preprocessing (`src/preprocess.py`):** When you drop an image into the app, it gets resized to `224x224` pixels, normalized, and converted into an array format that the neural network expects.
2. **Inference (`src/predict.py`):** The app builds a MobileNetV2 architecture shell and loads the pre-trained weights safely (`plant_model_weights.weights.h5`). It passes the image through the model to get probability scores across all trained classes.
3. **Remediation (`src/disease_info.py`):** Once the top class is identified, it maps the result to a dictionary of expert guidelines to show symptoms, prevention strategies, and treatments right on the screen.

---

## Tech Stack

* **Python** (3.10 / 3.11)
* **TensorFlow & Keras** (Deep Learning)
* **Streamlit** (Web Interface)
* **Pillow & NumPy** (Image Processing)

---

## Disclaimer

*This app is built for educational and demonstration purposes. For severe crop infections or agricultural emergencies, always consult a local agricultural extension office or a plant pathology expert.*

```

```
