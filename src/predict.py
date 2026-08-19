import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
import numpy as np
import json
import os

WEIGHTS_PATH = "models/plant_model_weights.weights.h5"
CLASS_INDICES_PATH = "class_indices.json"

print("Initializing model architecture and loading weights...")

if os.path.exists(CLASS_INDICES_PATH):
    with open(CLASS_INDICES_PATH, 'r') as f:
        class_indices = json.load(f)
    NUM_CLASSES = len(class_indices)
else:
    class_indices = None
    NUM_CLASSES = 38

base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights=None
)

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2),
    layers.Dense(NUM_CLASSES, activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

if os.path.exists(WEIGHTS_PATH):
    model.load_weights(WEIGHTS_PATH)
    print("Model weights loaded successfully!")
else:
    model = None
    print("Warning: Weights file not found in models/ folder!")

def predict_plant_disease(processed_image):
    if model is None or class_indices is None:
        raise ValueError("Model or class indices are not loaded properly.")

    predictions = model.predict(processed_image)

    predicted_index = np.argmax(predictions[0])

    confidence = float(predictions[0][predicted_index])

    predicted_class_name = class_indices.get(
        str(predicted_index),
        "Unknown Disease"
    )

    return predicted_class_name, confidence