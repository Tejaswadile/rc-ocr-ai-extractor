import argparse
import json
from pathlib import Path

from src.extractor import extract_rc_details


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract structured details from an RC document image."
    )
    parser.add_argument("image", help="Path to the RC image file")
    parser.add_argument(
        "--output",
        default="output/result.json",
        help="Path where extracted JSON should be saved",
    )
    parser.add_argument(
        "--show-text",
        action="store_true",
        help="Print raw OCR text before the structured JSON",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    result = extract_rc_details(args.image)

    if args.show_text:
        print("\n--- Raw OCR Text ---")
        print(result["raw_text"])

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result["details"], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(json.dumps(result["details"], indent=2, ensure_ascii=False))
    print(f"\nSaved output to: {output_path}")


if __name__ == "__main__":
    main()
