from PIL import Image

# open image file
img = Image.open('george-side.jpg')

# print image info
print(img.size)
print(img.format)

# crop image
area = (100, 100, 500, 500)
crop_img = img.crop(area)

# show image
img.show()
crop_img.show()
