import os
import zipfile

pptx_path = r"C:\Users\richa\.gemini\antigravity\brain\4a531a03-26ca-4221-85e0-135e48a6baf0\.user_uploaded\media_1793598741234_b7a379d0.pptx"
docx_path = r"C:\Users\richa\.gemini\antigravity\brain\4a531a03-26ca-4221-85e0-135e48a6baf0\.user_uploaded\media_1793598741153_b0299270.docx"

# Extract images from pptx (especially BMSCE logo)
with zipfile.ZipFile(pptx_path, 'r') as z:
    for name in z.namelist():
        if 'media' in name:
            print("PPTX media:", name)
            z.extract(name, 'extracted_pptx_media')

print("\nExtracted pptx media successfully!")

