from PIL import Image
img = Image.open('avantages-quil-y-a-a-grandir-dans-un-petit-village.jpg')
from PIL import ImageFilter
im1 = img.filter(ImageFilter.BLUR)
im1.show()
