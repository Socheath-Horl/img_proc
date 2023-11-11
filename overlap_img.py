from PIL import Image

# open image file
img = Image.open('george-side.jpg')
img1 = Image.open('google-icon@0.1x.png')

area = (0, 0, 240, 246)

img.paste(img1, area)

img.show()