from PIL import Image

img = Image.open('george-side.jpg')
print(img.mode)

r, g, b = img.split()

img.show()
r.show()
g.show()
b.show()
