from PIL import Image, ImageDraw, ImageFont
import os

def create_image():
    img = Image.new('RGB', (400, 200), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((20, 80), "JNTUA R23 Data Science Lab", fill=(255, 255, 0))
    target_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample.png')
    img.save(target_path)
    print(f"Sample image created successfully at: {os.path.abspath(target_path)}")

if __name__ == "__main__":
    create_image()
