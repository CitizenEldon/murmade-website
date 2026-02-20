from pypdf import PdfReader
import os

pdf_dir = "MurMade Product Labels and Branding"
files = os.listdir(pdf_dir)

for file in files:
    if file.endswith(".pdf"):
        print(f"--- {file} ---")
        try:
            reader = PdfReader(os.path.join(pdf_dir, file))
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            print(text.strip())
        except Exception as e:
            print(f"Error reading {file}: {e}")
        print("\n\n")

print("--- MurMade Logos Directory ---")
print(os.listdir("MurMade Logos"))
