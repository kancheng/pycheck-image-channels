from PIL import Image
img = Image.open('./carvana_img.jpg')
# Directly output the number of channels of the image
print("INFO. IMG.: carvana_img.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./carvana_mask.gif')
# Directly output the number of channels of the image
print("INFO. IMG.: carvana_mask.gif; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./coco128.jpg')
# Directly output the number of channels of the image
print("INFO. IMG.: coco128.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./mvtec_ad_img1.png')
# Directly output the number of channels of the image
print("INFO. IMG.: mvtec_ad_img1.png; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./mvtec_ad_img2.png')
# Directly output the number of channels of the image
print("INFO. IMG.: mvtec_ad_img2.png; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./mvtec_ad_mask.png')
# Directly output the number of channels of the image
print("INFO. IMG.: mvtec_ad_mask.png; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./salt_img.png')
# Directly output the number of channels of the image
print("INFO. IMG.: salt_img.png; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./salt_mask.png')
# Directly output the number of channels of the image
print("INFO. IMG.: salt_mask.png; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./brats_img_flair.jpg')
# Directly output the number of channels of the image
print("INFO. IMG.: brats_img_flair.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./brats_mask_seg.jpg')
# Directly output the number of channels of the image
print("INFO. IMG.: brats_mask_seg.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./brats_img_t1.jpg')
# Directly output the number of channels of the image
print("INFO. IMG.: brats_img_t1.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./brats_img_t1ce.jpg')
# Directly output the number of channels of the image
print("INFO. IMG.: brats_img_t1ce.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

img = Image.open('./brats_img_t2.jpg')
# Directly output the number of channels of the image
print("INFO. IMG.: brats_img_t2.jpg; Channels : ",len(img.split()), "; Details : ", img.split())

