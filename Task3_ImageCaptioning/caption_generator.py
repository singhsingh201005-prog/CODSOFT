import numpy as np
from PIL import Image
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model, load_model
from keras.preprocessing.image import load_img, img_to_array
import pickle

# Load the InceptionV3 model for feature extraction
def extract_features(filename):
    model = InceptionV3(weights='imagenet')
    model_new = Model(model.input, model.layers[-2].output)
    
    image = load_img(filename, target_size=(299, 299))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    features = model_new.predict(image, verbose=0)
    return features

# Load tokenizer and captioning model (you must train & save it earlier)
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
caption_model = load_model('caption_model.h5')

max_length = 34  # should match your trained model

# Generate caption
def generate_caption(photo, tokenizer, model, max_length):
    in_text = 'startseq'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = next((word for word, index in tokenizer.word_index.items() if index == yhat), None)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'endseq':
            break
    return in_text.replace('startseq', '').replace('endseq', '').strip()

# Example usage
if __name__ == "__main__":
    image_path = "example.jpg"  # Replace with your image
    photo = extract_features(image_path)
    description = generate_caption(photo, tokenizer, caption_model, max_length)
    print("Generated Caption:", description)
