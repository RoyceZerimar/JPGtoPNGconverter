from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
print(img.size)
small = (300, 300)
img.thumbnail(small)
img.save("thumbnail.jpg")
print(img.size)
