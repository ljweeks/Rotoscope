import sys
from PIL import Image

im = Image.open('dogLowRes.jpg')

pixels = im.load()

print(im.size)

ascii = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.        "
image = []
gray = Image.new(mode="RGB", size=(im.width, im.height))


for height in range(im.height):
    image.append("")
    for width in range(im.width):
        r, g, b = pixels[width, height]
        g = int((r + g + b) / 3)
        #print(g)
        char = ascii[int(g*len(ascii) / 255)]
        gray.putpixel((width, height), (g,g,g))
        image[height] += char

outfile = open('outFile.txt', 'w')
for line in image:
    outfile.write(line + '\n')
outfile.close()

gray.show()
gray = gray.save("gray.jpg")
