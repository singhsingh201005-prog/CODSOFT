from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

# Load the pre-trained model, processor, and tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Set device to GPU if available, else CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict_step(image_path):
    # Open image
    image = Image.open(image_path)

    # Prepare pixel values
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    # Generate caption ids
    output_ids = model.generate(pixel_values, max_length=16, num_beams=4)

    # Decode caption
    preds = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return preds

if __name__ == "__main__":
    # Path to your image
    image_path = "Task3_ImageCaptioning/example.jpg"
    caption = predict_step(image_path)
    print("Generated Caption:", caption)

