from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from utils.image_utils import preprocess_image, predict_class
import tensorflow as tf

app = Flask(__name__)

# Load pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Ensure uploads folder exists
UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Preprocess the image and predict
        img_array = preprocess_image(image_path)
        prediction = predict_class(model, img_array)

        return jsonify({
            "prediction": str(prediction[1]),  # Class label
            "confidence": float(prediction[2]), # Confidence score
            "image_url": f'/static/uploads/{filename}'   
        })
    else:
        return jsonify({"error": "Invalid file format"}), 400

if __name__ == "__main__":
    app.run(debug=True)