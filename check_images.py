from PIL import Image

for name in ['image1.png', 'image3.jpg', 'image4.png']:
    path = f'extracted_pptx_media/ppt/media/{name}'
    im = Image.open(path)
    print(name, im.size, im.format)

