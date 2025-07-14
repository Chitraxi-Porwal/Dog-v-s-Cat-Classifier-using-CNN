from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import datetime
import csv

app = Flask(__name__)
model = load_model("catvsdog.h5")

LOG_FILE = "prediction_log.csv"

# Create log file if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([file.filename, label, confidence, datetime.datetime.now()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    files = request.files.getlist('images')
    results = []

    for file in files:
        if file.filename == '':
            continue

        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        img = load_img(filepath, target_size=(256, 256))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prob = model.predict(img_array)[0][0]
        label = "Dog" if prob > 0.5 else "Cat"
        confidence = round(prob * 100, 2) if prob > 0.5 else round((1 - prob) * 100, 2)

        # Log predictions
        with open(LOG_FILE, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([file.filename, label, confidence, datetime.datetime.now()])

        results.append({
            "filename": file.filename,
            "filepath": filepath,
            "label": label,
            "confidence": confidence
        })

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
