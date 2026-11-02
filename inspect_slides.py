import os
from pptx import Presentation

pptx_path = r"C:\Users\richa\.gemini\antigravity\brain\4a531a03-26ca-4221-85e0-135e48a6baf0\.user_uploaded\media_1793598741234_b7a379d0.pptx"
prs = Presentation(pptx_path)

print(f"Total slides in user template: {len(prs.slides)}")
print(f"Slide dimensions: width={prs.slide_width.inches} in, height={prs.slide_height.inches} in")

for idx, slide in enumerate(prs.slides):
    print(f"\n--- Slide {idx+1} ---")
    for shape in slide.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text.strip().replace('\n', ' | ')
            if text:
                print(f"  [Text]: {text[:120]}")
        elif shape.shape_type == 13: # Picture
            print(f"  [Picture]: {shape.name}")

