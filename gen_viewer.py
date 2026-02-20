import os
import glob

# gather some images
images = glob.glob("MurMade Pictures/*.[jp][pn]g")
images.sort()

# let's just use the first 50 images to avoid overwhelming the subagent, plus a random sample of remaining
selected_images = images[:60]

html = "<html><body><h1>MurMade Pictures</h1><ul style='list-style:none;'>"
for img in selected_images:
    html += f"<li><h3>{os.path.basename(img)}</h3><img src='{img}' style='width:300px; height:auto;'/></li>"
html += "</ul></body></html>"

with open("image_viewer.html", "w") as f:
    f.write(html)
