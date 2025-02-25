from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import cv2
import numpy as np
model = load_model('path_to_your_model.h5')
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

        img = cv2.resize(img, (img_height, img_width))
        img = np.expand_dims(img, axis=0) / 255.0
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions, axis=1)

        return jsonify({'predicted_class': int(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True)
