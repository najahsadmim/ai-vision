import sys
from transformers import pipeline
from PIL import Image

captioner= pipeline("image-text-to-text", model="Salesforce/blip-image-captioning-base")

def genCaption(image_path):
    try:
        img=Image.open(image_path).convert('RGB')
        print("Analysing...")
        result=captioner(img, text="a picture of")
        return result[0]['generated_text']
    
    except Exception as e:
        return f"Error: {e}"
    
if __name__=="__main__":
    image_file="datathon-prize.png"
    description=genCaption(image_file)
    print(f"\nResult: {description.capitalize()}")
    

