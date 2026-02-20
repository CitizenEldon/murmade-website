import os
import glob

# gather some images
images = glob.glob("MurMade Pictures/*.[jp][pn]g")
images.sort()

html = "<html><body><h1>MurMade Pictures 2</h1><ul style='list-style:none;'>"
for img in images:
    # Only pick images that don't have "COLLAGE" in the name to help out
    if "COLLAGE" not in img.upper() and "LABEL" not in img.upper() and "LOGO" not in img.upper():
        html += f"<li><h3>{os.path.basename(img)}</h3><img src='{img}' style='width:300px; height:auto;'/></li>"
html += "</ul></body></html>"

with open("image_viewer_2.html", "w") as f:
    f.write(html)
