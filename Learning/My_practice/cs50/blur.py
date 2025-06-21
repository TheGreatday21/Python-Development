from PIL import Image, ImageFilter
#the bmp file format makes images binary 
before =  Image.open("v.bmp")

after = before.filter(ImageFilter.BoxBlur(10))
after.save("blur_v.bmp")
