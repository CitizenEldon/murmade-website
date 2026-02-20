import os
from PIL import Image

src_dir = "MurMade Logos"
dst_dir = "public/assets/images"

os.makedirs(dst_dir, exist_ok=True)

for filename in os.listdir(src_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        src_path = os.path.join(src_dir, filename)
        base_name, _ = os.path.splitext(filename)
        dst_path = os.path.join(dst_dir, base_name + ".webp")
        
        try:
            img = Image.open(src_path)
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                background.save(dst_path, "WEBP", quality=80)
            else:
                img.save(dst_path, "WEBP", quality=80)
            print(f"Converted logo {filename} to {base_name}.webp")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
