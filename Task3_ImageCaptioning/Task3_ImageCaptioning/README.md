# Task 3 – Image Captioning 🖼️🤖

This project uses deep learning to generate natural language captions for images using InceptionV3 + LSTM.

## ⚙️ How it works

- **CNN (InceptionV3)** extracts image features
- **Tokenizer + LSTM model** generates captions
- Pretrained model required: `caption_model.h5` and `tokenizer.pkl`

## 🛠️ How to run

1. Place your image (e.g., `example.jpg`) in the same folder
2. Run:


3. You'll see a generated caption in the output

## 📦 Requirements

- TensorFlow / Keras
- NumPy
- Pillow
