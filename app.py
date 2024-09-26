import easyocr
import re
import gradio as gr

# Initialize OCR model for English and Hindi
reader = easyocr.Reader(['en', 'hi'], gpu=False)

# Function to extract text from the uploaded image
def extract_text_from_image(image):
    result = reader.readtext(image, detail=0)  # Extract text without bounding box details
    extracted_text = ' '.join(result)  # Combine list of text into a single string
    return extracted_text

# Function to search for a keyword in the extracted text
def search_keyword(text, keyword):
    matches = re.findall(rf"\b{re.escape(keyword)}\b", text, flags=re.IGNORECASE)
    if matches:
        return f"Keyword '{keyword}' found {len(matches)} time(s)."
    else:
        return f"Keyword '{keyword}' not found."

# Gradio interface function to handle OCR and keyword search
def process_image(image, keyword):
    extracted_text = extract_text_from_image(image)  # OCR process
    search_result = search_keyword(extracted_text, keyword)  # Keyword search
    return extracted_text, search_result

# Gradio Interface
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="filepath", label="Upload an Image"), 
        gr.Textbox(label="Enter a Keyword to Search")
    ],
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Search Results")
    ],
    title="Hindi and English OCR with Keyword Search",
    description="Upload an image with text in Hindi or English, and search for specific words within the extracted text.",
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()
