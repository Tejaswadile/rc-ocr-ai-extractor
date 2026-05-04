RC OCR AI Extractor
About the Project

This project is designed to automate the extraction of important details from vehicle RC (Registration Certificate) documents using AI.

In many real-world scenarios, RC data is entered manually, which is time-consuming and prone to errors. To address this, a Python-based system has been developed that reads RC images and converts them into structured, usable data.

Objective

The main objective of this project is to:

Reduce manual data entry
Improve accuracy
Save time and effort

The system extracts key information such as:

Owner Name
Vehicle Number
Engine Number
Chassis Number
How It Works

The system follows a step-by-step workflow:

Upload an image of the RC document
Preprocess the image using OpenCV (grayscale, blur, thresholding)
Extract text using Tesseract OCR
Clean and process the extracted text
Identify key details using pattern matching (Regex)
Convert the extracted data into structured JSON format
Technologies Used
Python
OpenCV
Tesseract OCR
Regular Expressions (Regex)
AI tools such as ChatGPT and Claude for logic refinement
Key Features
Converts RC images into machine-readable text
Automatically extracts important vehicle details
Reduces manual workload
Produces structured output in JSON format
Simple and scalable implementation
How to Run
Install dependencies
pip install -r requirements.txt
Install Tesseract OCR
Windows: Install Tesseract and add it to system PATH
Linux/Mac:
sudo apt install tesseract-ocr
Run the script
python app.py
Sample Output
{
  "Owner Name": "Rahul Sharma",
  "Vehicle Number": "MH12AB1234",
  "Engine Number": "ENG123456",
  "Chassis Number": "CHS987654"
}
Use Case

This project can be applied in:

RTO systems
Vehicle management platforms
Data automation workflows

It helps reduce manual effort and improves processing efficiency.

Future Improvements
Develop a web interface using Flask
Enhance accuracy using deep learning models
Add support for multiple languages
Contact

For demonstration or queries, you can reach out for further details.
7709328570
