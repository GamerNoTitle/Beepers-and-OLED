import sys
from PIL import Image

argv = sys.argv
if(len(sys.argv)<2):
    print("Please input image file name.")
    print("For example, input face.png, output faceMap.py")
    print(" python3 gengerate.py face")
    sys.exit(-1)
# open image file
image = Image.open(sys.argv[1])
width,height = image.size
print('image size',width,height)
pixels = image.load()

# open file
f = open(sys.argv[1]+"Map.py", "w")
f.write(sys.argv[1]+"Map = [\n")

for y in range(height):
    f.write("'")
    for x in range(width):
         # print(x,y,pixels[x,y])
         if(pixels[x,y][0]<=0): # black
             f.write('1')
         else:
            f.write('0')
    f.write("',\n")
f.write("]\n")