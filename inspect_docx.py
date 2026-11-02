import docx

docx_path = r"C:\Users\richa\.gemini\antigravity\brain\4a531a03-26ca-4221-85e0-135e48a6baf0\.user_uploaded\media_1793598741153_b0299270.docx"
doc = docx.Document(docx_path)

print(f"Total paragraphs in reference docx: {len(doc.paragraphs)}")
print(f"Total tables: {len(doc.tables)}")

for i in range(min(25, len(doc.paragraphs))):
    text = doc.paragraphs[i].text.strip()
    if text:
        print(f"P{i+1}: {text[:100]}")

