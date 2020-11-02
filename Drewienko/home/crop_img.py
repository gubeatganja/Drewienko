from PIL import Image

im = Image.open('Screenshot_2.png')
width, height = im.size
if width > height:
    cropped = im.crop(((width-height)/2, 0, height+(width-height)/2, height))
else:
    cropped = im.crop((0, (height-width)/2, height, width+(height-width)/2))
cropped.show()