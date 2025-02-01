# Image Classification

This project is a simple web application for image classification using a pre-trained MobileNetV2 model. Users can upload an image, and the application will return a predicted label for the image along with a confidence score.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/brianlh9/image_classification.git
    cd image_classification
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Upload an image and see the classification result.

## Project Structure

- `app.py`: Main Flask application file.
- `requirements.txt`: List of Python packages required for the project.
- `static`: Static files (CSS, JavaScript, uploaded images).
- `templates`: HTML templates.
- `utils`: Utility functions for image preprocessing and prediction.

