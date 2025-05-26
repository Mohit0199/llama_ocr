# Llama OCR - Image Text Extraction Tool

A powerful web application that uses Llama 3.2 Vision model to extract and analyze text from images. Built with Streamlit and Ollama, this tool provides an intuitive interface for OCR (Optical Character Recognition) tasks.

## Features

- 🖼️ Upload images in PNG, JPG, or JPEG formats
- 🔍 Extract text from images using Llama 3.2 Vision model
- 📝 Structured text output in Markdown format
- 🎯 Clear and user-friendly interface
- 🚀 Real-time processing and results display

## Prerequisites

- Python 3.x
- Streamlit
- Ollama
- Pillow (PIL)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_OCR_Project
```

2. Install the required dependencies:
```bash
pip install streamlit ollama pillow
```

3. Make sure you have Ollama installed and running locally with the Llama 3.2 Vision model:
```bash
ollama pull llama3.2-vision:latest
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload an image using the file uploader

4. Click the "Extract Text" button to process the image

5. View the extracted text in the results section

## How It Works

The application uses the following workflow:
1. User uploads an image through the Streamlit interface
2. The image is processed using the Llama 3.2 Vision model via Ollama
3. The model analyzes the image and extracts text content
4. Results are displayed in a structured Markdown format

## Features in Detail

- **Image Upload**: Supports common image formats (PNG, JPG, JPEG)
- **Text Extraction**: Uses advanced AI vision model for accurate text recognition
- **Clear Functionality**: Easy way to reset and start over
- **Error Handling**: Graceful error management for failed processing attempts
- **Responsive Design**: Clean and intuitive user interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with Streamlit
- Powered by Ollama and Llama 3.2 Vision model
- Uses Pillow for image processing 