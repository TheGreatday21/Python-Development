
#this outlines all the boundaries of the image 
from PIL import Image,ImageFilter
#PIL = Python Image Library

before = Image.open("v.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("edege_v.bmp")


