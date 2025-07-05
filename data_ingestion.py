import os
import requests
import zipfile
import PyPDF2
import re

# Dataset zip details
DATA_URL = "https://github.com/BollywoodData/Bollywood-Data/archive/refs/heads/master.zip"
DATA_DIR = os.path.join("data")
ZIP_PATH = os.path.join(DATA_DIR, "bollywood_data.zip")


# ✅ 1. Download & extract zip file
def download_and_extract():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(ZIP_PATH):
        print("📥 Downloading dataset...")
        response = requests.get(DATA_URL)
        with open(ZIP_PATH, "wb") as f:
            f.write(response.content)
        print("✅ Downloaded.")

        print("📦 Extracting...")
        with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(DATA_DIR)
        print("✅ Extracted.")
    else:
        print("📁 Dataset already downloaded and extracted.")


# ✅ 2. Extract plain text from a PDF script
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


# ✅ 3. Extract dialogue blocks from script
def extract_dialogue_blocks(text):
    pattern = r'([A-Z][A-Z ]{1,30})'
    splits = re.split(pattern, text)
    blocks = []
    i = 1
    while i < len(splits):
        character = splits[i].strip()
        if character and character.isupper():
            dialogue = splits[i + 1].replace('\n', ' ').strip() if (i + 1) < len(splits) else ""
            blocks.append((character, dialogue))
        i += 2
    return blocks


# ✅ 4. Run this script to test everything together
if __name__ == "__main__":
    download_and_extract()
    pdf_path = os.path.join(DATA_DIR, "Bollywood-Data-master", "scripts-data", "Queen.pdf")

    if not os.path.exists(pdf_path):
        print(f"❌ Script not found: {pdf_path}")
    else:
        print(f"📄 Extracting from: {pdf_path}")
        text = extract_text_from_pdf(pdf_path)
        print(f"📜 Text length: {len(text)}")

        blocks = extract_dialogue_blocks(text)
        print(f"🗣 Extracted {len(blocks)} dialogue blocks.")

        print("🔹 Sample:")
        for b in blocks[:3]:
            print(f"{b[0]}: {b[1][:80]}...")