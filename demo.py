import os

colpath = []
path = '.'

for root, dirs, files in os.walk(path):
    print("ROOT : ", root)
    print("DIRS : ",dirs)
    print("FILES : ", files)

for root, dirs, files in os.walk(path):
    for img in files:
        if img.endswith((".png", ".jpg", ".jpeg", ".bmp")):
            # print("FILE NAME : ", img)
            colpath.append(root + "/" + img)

print("ALL PATH : ", colpath)

from PIL import Image

for c in colpath:
    img = Image.open(c)
    # Directly output the number of channels of the image
    print("INFO. IMG.: carvana_img.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

# └─img
#     ├─a
#     └─b
#         └─ba