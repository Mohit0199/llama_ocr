import streamlit as st
import ollama
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Llama OCR",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("Llama OCR")
st.markdown("Extract text from images using Llama 3.2 Vision!")
st.markdown("---")

# Clear button (now just below title, no columns)
if st.button("Clear 🗑️"):
    if 'ocr_result' in st.session_state:
        del st.session_state['ocr_result']
    st.rerun()

# File uploader (not in sidebar anymore)
uploaded_file = st.file_uploader("Upload an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    if st.button("Extract Text 🔍", type="primary"):
        with st.spinner("Processing image..."):
            try:
                response = ollama.chat(
                    model='llama3.2-vision',
                    messages=[{
                        'role': "user",
                        'content': "Analyze the text in the provided image. Extract all the content.",
                        'images': [uploaded_file.getvalue()]
                    }]
                )
                st.session_state['ocr_result'] = response.message.content
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")

# Output area
if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else:
    st.info("Upload an image and click 'Extract Text' to see the results here.")
