from PIL import Image

# open image file
img = Image.open('george-side.jpg')

# print image info
print(img.size)
print(img.format)
# show image
img.show()
