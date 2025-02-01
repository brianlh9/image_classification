from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

def preprocess_image(img_path):
    """Preprocess image for the model (resize, normalize)"""
    img = image.load_img(img_path, target_size=(224, 224))  # Resize image to fit model input
    img_array = image.img_to_array(img)  # Convert image to numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)  # Preprocess for MobileNetV2
    return img_array

def predict_class(model, img_array):
    """Predict class using pre-trained model"""
    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)
    return decoded_predictions[0][0]  # Class label, confidence score
