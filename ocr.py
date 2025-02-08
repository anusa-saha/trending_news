import requests
import base64
import tkinter as tk
from tkinter import filedialog

API_KEY = "AIzaSyBT-kDQY5tMoPAsgvJI9ze40NYIB4fko3U"

if not API_KEY:
    print("Error: API key not set. Please set GOOGLE_APPLICATION_CREDENTIALS environment variable.")
    exit()

def upload_image():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    return file_path

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def extract_text_from_image(image_path):    
    base64_image = encode_image(image_path)

    
    url = f"https://vision.googleapis.com/v1/images:annotate?key={API_KEY}"

    
    payload = {
        "requests": [{
            "image": {"content": base64_image},
            "features": [{"type": "TEXT_DETECTION"}]
        }]
    }

   
    response = requests.post(url, json=payload)

    
    if response.status_code == 200:
        result = response.json()
        try:
            extracted_text = result["responses"][0]["textAnnotations"][0]["description"]
            print("\nExtracted Text:\n", extracted_text)
            return extracted_text
        except KeyError:
            print("\nNo text detected.")
            return None
    else:
        print("\nError:", response.status_code, response.text)
        return None

def main():
    """Main function to handle image selection and OCR processing."""
    print("Select an image for OCR processing...")
    image_path = upload_image()

    if not image_path:
        print("No image selected.")
        return

    print("\nProcessing Image...")
    extract_text_from_image(image_path)

if __name__ == "__main__":
    main()
