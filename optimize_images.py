import os
from PIL import Image

src_dir_1 = "MurMade Pictures"
src_dir_2 = "MurMade Product Labels and Branding"
dst_dir = "public/assets/images"

os.makedirs(dst_dir, exist_ok=True)

# Process images
for src_dir in [src_dir_1, src_dir_2]:
    if not os.path.exists(src_dir):
        continue
    for filename in os.listdir(src_dir):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            src_path = os.path.join(src_dir, filename)
            base_name, _ = os.path.splitext(filename)
            dst_path = os.path.join(dst_dir, base_name + ".webp")
            
            # Avoid re-processing
            if os.path.exists(dst_path):
                continue
                
            try:
                img = Image.open(src_path)
                # Convert to RGB if necessary (e.g. RGBA to WebP)
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[3]) # 3 is the alpha channel
                    background.save(dst_path, "WEBP", quality=80)
                else:
                    img.save(dst_path, "WEBP", quality=80)
                print(f"Converted {filename} to {base_name}.webp")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")
