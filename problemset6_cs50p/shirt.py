import sys
import os.path
from PIL import Image,ImageOps

if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)==2:
    sys.exit("Enter Output file")
elif not sys.argv[1].endswith((".jpeg",".JPEG",".jpg",".JPG",".png",".PNG")):
    sys.exit("Enter Input file in jpg,jpeg or png format")
elif not sys.argv[2].endswith((".jpeg",".JPEG",".jpg",".JPG",".png",".PNG")):
    sys.exit("Enter name of Output file to create in jpg,jpeg or png format")
elif os.path.splitext(sys.argv[1])[1]!=os.path.splitext(sys.argv[2])[1]:
    sys.exit("Both files should be in same format")

im=Image.open("shirt.png")
im2=Image.open(sys.argv[1])
im2=ImageOps.fit(im2,im.size)
im2.paste(im,(0,-30),mask=im)
im2.save(fp=sys.argv[2])