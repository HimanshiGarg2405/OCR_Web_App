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

# Function to highlight the keyword in the extracted text
def highlight_keyword(text, keyword):
    # Use regex to find all occurrences of the keyword and wrap them in <mark> for highlighting
    highlighted_text = re.sub(rf"({re.escape(keyword)})", r'<mark>\1</mark>', text, flags=re.IGNORECASE)
    return highlighted_text

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
    highlighted_text = highlight_keyword(extracted_text, keyword)  # Highlight keyword in text
    search_result = search_keyword(extracted_text, keyword)  # Keyword search
    return highlighted_text, search_result

# Gradio Interface
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="filepath", label="Upload an Image"), 
        gr.Textbox(label="Enter a Keyword to Search")
    ],
    outputs=[
        gr.HTML(label="Extracted Text with Highlighted Keyword"),  # Use HTML output to show highlighted text
        gr.Textbox(label="Search Results")
    ],
    title="Hindi and English OCR with Keyword Search",
    description="Upload an image with text in Hindi or English, and search for specific words within the extracted text.",
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()
