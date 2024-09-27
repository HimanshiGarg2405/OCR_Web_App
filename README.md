# OCR Web Application with Keyword Search

This web application uses **EasyOCR** to extract text from images in both Hindi and English, with a feature to search for keywords in the extracted text. The interface is built using **Gradio**, and the project is intended to be run locally and deployed on **Hugging Faces**.

## Features

- **Image Upload**: Supports JPEG and PNG formats for image uploads.
- **OCR Functionality**: Extracts text from the uploaded image using EasyOCR, supporting both Hindi and English.
- **Keyword Search**: Allows users to search for specific keywords in the extracted text.

## Prerequisites

Before running the application locally or deploying it, ensure you have the following installed:

- **Python 3.10+**
- **Git**
- **Pip** (Python package manager)
- **Virtual Environment** (optional but recommended)

## 1. Environment Setup

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/HimanshiGarg2405/OCR_Web_App.git
cd OCR_Web_App
```

## Set Up a Virtual Environment (Optional but Recommended)

It is a good practice to create a virtual environment to manage project dependencies.

### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

Install the necessary dependencies listed in the requirements.txt file.

```bash
pip install -r requirements.txt
```

This will install the following packages:

- **torch**: For handling machine learning operations.
- **torchvision**: For computer vision operations.
- **easyocr**: The OCR library used for text extraction.
- **gradio**: The frontend framework for building the web interface.

## 2. Running the Application Locally

After setting up the environment and installing the required packages, you can run the application on your local machine.

### Command to Run the Application

```bash
python app.py
```

## Accessing the Web Application

Once the app is running, it will be accessible at `http://localhost:7860/` by default. Open this URL in your web browser to use the OCR application.

## 3. Application Workflow

1. Upload an image (either a PNG or JPEG file).
2. The application will extract text from the image using **EasyOCR**.
3. Enter a keyword to search for specific terms in the extracted text.
4. The extracted text and the results of the keyword search will be displayed on the interface.

## 4. Deployment on Hugging Faces

You can deploy the application on Hugging Faces using the **Gradio** interface. Here's how to do that:

### Steps for Deployment on Hugging Faces:

1. **Create a Hugging Faces Account**:
   If you don’t already have a Hugging Faces account, sign up at [https://huggingface.co/join](https://huggingface.co/join).

2. **Create a New Space**:
   - Go to the Hugging Faces homepage and navigate to "Spaces" from your account dashboard.
   - Create a new space, choose the **Gradio** template, and set the repository to **public**.

3. **Upload Project Files**:
   Upload all the necessary files from your local project, including the `app.py`, `requirements.txt`, and any other project-specific files.

4. **Configure the `app.py` File**:
   Ensure that the `app.py` is set up to use Gradio, and adjust the app to use the Hugging Faces environment.

5. **Push the Code to Hugging Faces**:

   You can either drag and drop files to your new space or push the code using Git:

```bash
   git remote add huggingface https://huggingface.co/spaces/<your_space_name>
   git push huggingface main
```

## Deploy

Once the files are uploaded, Hugging Faces will automatically start the deployment process. Your web application will be available on a unique URL that Hugging Faces provides.

## 5. Directory Structure

The following is an example of how the project directory is structured:

```plaintext
OCR_Web_App/
│
├── app.py               # Main Python file to run the application
├── requirements.txt      # Dependencies required for the project
└── README.md             # This file
```

## Testing and Debugging

- To test locally, upload various images containing text in Hindi or English and check for successful text extraction.
- Ensure the Gradio interface is displaying results properly and handle any errors that occur during the keyword search or OCR extraction.
- For deployment, test the Hugging Faces space by uploading images and performing keyword searches.

## 7. Contributing

Feel free to submit issues or pull requests to improve the project. All contributions are welcome!
