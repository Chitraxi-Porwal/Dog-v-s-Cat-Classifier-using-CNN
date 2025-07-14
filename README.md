# 🐱🐶 Cat vs Dog Image Classifier - Flask Web App

A deep learning web application built using **Flask** that classifies uploaded images as either a **Cat** or a **Dog**, based on a trained **Convolutional Neural Network (CNN)** model.

## 📸 Demo

![pred 2](https://github.com/user-attachments/assets/28d12145-83ea-4f2e-9569-1457ff94c722)
![pred 1](https://github.com/user-attachments/assets/9353dd01-14fe-40c6-91d1-626195a0618b)

## 🔍 Features

- ✅ Upload one or **multiple images**
- ✅ Predicts whether each image is a **Cat 🐱** or **Dog 🐶**
- ✅ Displays **confidence score** with a visual progress bar
- ✅ Supports drag-and-drop file uploads (via browser)
- ✅ Stores each prediction in a **CSV log file**
- ✅ Lightweight, easy to run locally
- ✅ Simple HTML/CSS frontend with responsive design
- ✅ Emoji support in UI (with optional CSV-safe logging)

## 🧠 Model Details

- Built using **TensorFlow & Keras**
- Model architecture:
  - 3 × `Conv2D` + `MaxPooling2D`
  - Flatten + Dense layers
  - Dropout layers for regularization
  - Final `sigmoid` layer for binary classification
- Trained on the [Kaggle Dogs vs Cats dataset](https://www.kaggle.com/datasets/salader/dogs-vs-cats)
- Saved model: `catvsdog.h5`

## 🚀 How to Run Locally

### 🔧 1. Clone this repository

```bash
git clone https://github.com/your-username/cat-vs-dog-classifier.git
cd cat-vs-dog-classifier

📦 2. Create & activate virtual environment (recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows

📥 3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

▶️ 4. Run the Flask app
bash
Copy
Edit
python app.py
Open in your browser: http://127.0.0.1:5000

📁 Project Structure
cat-vs-dog-classifier/
│
├── app.py                  # Flask backend
├── catvsdog.h5             # Trained CNN model
├── prediction_log.csv      # CSV log of predictions
├── requirements.txt        # Python dependencies
│
├── templates/
│   ├── index.html          # Upload form UI
│   └── result.html         # Prediction results
│
├── static/
│   ├── style.css           # CSS styling
│   └── demo.png            # (Optional) UI screenshot
📝 Logging Format

Each prediction is logged in prediction_log.csv:
Filename	Prediction	Confidence (%)	Timestamp
cat1.jpg	Cat	98.22	2025-07-14 11:10:32
dog2.jpg	Dog	95.64	2025-07-14 11:11:45

⚠️ Emojis are shown only in the UI to avoid encoding issues in CSV.

📦 Requirements
Python 3.7+
Flask
TensorFlow
NumPy
Pillow

Install via:
pip install -r requirements.txt

✨ Future Improvements
Add drag-and-drop support
Upload via webcam
Deploy on Render, Railway, or Hugging Face Spaces
Add visual explanations (Grad-CAM)

👨‍💻 Author
Chitraxi Porwal
📧 chitraxiporwal2004@gmail.com
