import re

from src.ocr import extract_text


FIELD_PATTERNS = {
    "Owner Name": [
        r"(?:owner(?:'s)?\s*name|name)\s*[:\-]?\s*([A-Z][A-Z\s.]{2,})",
    ],
    "Vehicle Number": [
        r"\b([A-Z]{2}\s?\d{1,2}\s?[A-Z]{1,3}\s?\d{4})\b",
        r"(?:registration\s*no|regn\.?\s*no|vehicle\s*no)\s*[:\-]?\s*([A-Z0-9\s-]{6,15})",
    ],
    "Engine Number": [
        r"(?:engine\s*no|eng\.?\s*no)\s*[:\-]?\s*([A-Z0-9-]{5,25})",
    ],
    "Chassis Number": [
        r"(?:chassis\s*no|chasis\s*no|vin)\s*[:\-]?\s*([A-Z0-9-]{5,25})",
    ],
}


def clean_text(text):
    text = text.upper()
    text = re.sub(r"[|]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_value(value):
    return re.sub(r"\s+", " ", value).strip(" :-")


def find_first_match(text, patterns):
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return normalize_value(match.group(1))
    return None


def parse_rc_details(text):
    cleaned = clean_text(text)
    details = {}

    for field, patterns in FIELD_PATTERNS.items():
        details[field] = find_first_match(cleaned, patterns)

    if details["Vehicle Number"]:
        details["Vehicle Number"] = re.sub(r"[\s-]+", "", details["Vehicle Number"])

    return details


def extract_rc_details(image_path):
    raw_text = extract_text(image_path)
    return {
        "raw_text": raw_text,
        "details": parse_rc_details(raw_text),
    }
