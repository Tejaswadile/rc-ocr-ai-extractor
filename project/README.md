# RC OCR AI Extractor

Python project for extracting structured vehicle Registration Certificate details from RC document images using OpenCV, Tesseract OCR, and Regex.

## Features

- Preprocesses RC images for better OCR accuracy
- Extracts text using Tesseract OCR
- Finds owner name, vehicle number, engine number, and chassis number
- Saves structured JSON output
- Provides a simple command-line workflow

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── extractor.py
│   ├── ocr.py
│   └── preprocessing.py
├── samples/
│   └── .gitkeep
└── output/
    └── .gitkeep
```

## Requirements

- Python 3.9+
- Tesseract OCR installed on your system

## Install

```bash
pip install -r requirements.txt
```

### Install Tesseract OCR

Windows:

Install Tesseract OCR and add it to your system PATH.

Linux:

```bash
sudo apt install tesseract-ocr
```

macOS:

```bash
brew install tesseract
```

## Run

Place an RC image inside the `samples` folder, then run:

```bash
python app.py samples/rc_sample.jpg
```

To save output to a custom path:

```bash
python app.py samples/rc_sample.jpg --output output/result.json
```

## Sample Output

```json
{
  "Owner Name": "Rahul Sharma",
  "Vehicle Number": "MH12AB1234",
  "Engine Number": "ENG123456",
  "Chassis Number": "CHS987654"
}
```

## Future Improvements

- Add a Flask web interface
- Improve extraction using ML or deep learning models
- Add multilingual OCR support
- Support more RC layouts and states
