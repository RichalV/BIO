from pptx import Presentation

pptx_path = r"C:\Users\richa\.gemini\antigravity\brain\4a531a03-26ca-4221-85e0-135e48a6baf0\.user_uploaded\media_1793598741234_b7a379d0.pptx"
prs = Presentation(pptx_path)

for idx, slide in enumerate(prs.slides):
    print(f"=== SLIDE {idx+1} ===")
    for s_idx, shape in enumerate(slide.shapes):
        if shape.has_text_frame:
            print(f"  Shape {s_idx} ({shape.name}):")
            for p_idx, p in enumerate(shape.text_frame.paragraphs):
                text = p.text.strip()
                if text:
                    print(f"    P{p_idx}: {text}")

