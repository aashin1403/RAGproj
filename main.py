import pypdf
import argparse
import sys
import os

parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
parser.add_argument("pdf_file", help="Path to the PDF file to extract text from.")
args = parser.parse_args()

# Check if file exists before trying to open it
if not os.path.exists(args.pdf_file):
    print(f"Error: file '{args.pdf_file}' not found")
    sys.exit(1)

# Check if it's actually a PDF
if not args.pdf_file.endswith(".pdf"):
    print(f"Error: '{args.pdf_file}' is not a PDF file")
    sys.exit(1)

with open(args.pdf_file, "rb") as file:
    reader = pypdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

print(text)

