DISEASE_INFO = {
    "Tomato___Target_Spot": {
        "plant": "Tomato",
        "disease": "Target Spot",
        "description": "Target spot is a fungal disease caused by Corynespora cassiicola that affects tomato leaves, stems, and fruit, leading to reduced yields.",
        "symptoms": "Small brown to black spots on leaves that can expand with concentric rings, resembling a target. Severe infection causes leaf yellowing and premature defoliation.",
        "prevention": "Use certified disease-free seeds, practice crop rotation with non-host plants, and avoid overhead sprinkler irrigation.",
        "treatment": "Apply appropriate copper-based or systemic fungicides at the first sign of disease symptoms. Remove and destroy heavily infected plant debris."
    },
    "Tomato___Late_blight": {
        "plant": "Tomato",
        "disease": "Late Blight",
        "description": "Late blight is a devastating fungal-like disease caused by Phytophthora infestans that can destroy an entire crop in a matter of days under wet conditions.",
        "symptoms": "Large, dark water-soaked spots on leaves or stems that rapidly turn brown or black. White fungal growth may appear on the underside of leaves in humid weather.",
        "prevention": "Ensure proper plant spacing for good airflow, keep foliage as dry as possible, and plant resistant varieties where available.",
        "treatment": "Remove and destroy infected plants immediately to prevent spores from spreading. Apply recommended preventative fungicides during wet weather."
    },
    "Tomato___healthy": {
        "plant": "Tomato",
        "disease": "Healthy",
        "description": "Your plant appears to be in excellent condition with no visible signs of pathogen infection or environmental stress.",
        "symptoms": "Vibrant green leaves, steady growth, no spots, discoloration, or wilting.",
        "prevention": "Maintain regular watering at the base of the plant, ensure adequate sunlight, and provide balanced soil nutrients.",
        "treatment": "No treatment required! Continue your current healthy gardening practices."
    }
}

def get_disease_details(class_name):
    default_info = {
        "plant": class_name.split("___")[0].replace("_", " ") if "___" in class_name else "Plant",
        "disease": class_name.split("___")[1].replace("_", " ") if "___" in class_name else class_name,
        "description": "This is a plant condition identified by our AI model. Regular monitoring is recommended.",
        "symptoms": "Visual abnormalities, spotting, discoloration, or changes in leaf texture.",
        "prevention": "Practice good garden hygiene, ensure proper spacing, avoid overwatering, and remove weeds.",
        "treatment": "Consult a local agricultural extension office or plant nursery for professional diagnosis and specific local treatment options."
    }

    return DISEASE_INFO.get(class_name, default_info)