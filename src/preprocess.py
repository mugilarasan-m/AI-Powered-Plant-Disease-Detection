import tensorflow as tf
from PIL import Image
import numpy as np

def prepare_image(image_path_or_file):
    if isinstance(image_path_or_file, str):
        image = Image.open(image_path_or_file)
    else:
        image = Image.open(image_path_or_file)

    image = image.convert("RGB")
    image = image.resize((224, 224))

    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array