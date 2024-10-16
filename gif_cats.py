#pip install pillow
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "img\cats.gif", save_all=True, append_images=images[1:], duration=100, loop=0
)

# py.exe gif_cats.py img\cat1.gif img\cat2.gif img\cat3.gif img\cat4.gif img\cat5.gif img\cat6.gif