# AI Vision: Image Captioning with BLIP

A Python-based Computer Vision tool using Salesforce BLIP model to generate descriptive texts from provided image. This project demonstrates local inference of Multimodal Large Language Models (MLLMs). This project uses the 'transformers' library to build a vision-to-text pipeline. It takes a local image file as input and processes it through a pre-trained transformer model to output a human-readable description.

**Tech Stack:**
- Language: Python
- Framework: Hugging Face Transformers
- Model: Salesforce BLIP
- Libraries: PIL (pillow), PyTorch

**Features:**
- Local Inference: Runs entirely on your machine (no API keys required).
- Multimodal Processing: Uses the 'image-text-to-text' task for advanced context awareness.
- Error Handling: Robust image verification and exception catching.

**Future Improvements:**
- Build a browser-based UI where you upload an image and see the caption appear instantly.
- Instead of a fixed prompt like "a photography of", allow the user to type a question like "How many bags are there?" or "What is the currency symbol?"
- Take the text result and pipe it into a library like pyttsx3 to generate speech (almost like an AI Virtual Assistant)
- Load the model at higher precision (float) to make execution faster, and cut down on excessive RAM usage.

