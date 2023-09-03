# http://www.pythonchallenge.com/pc/return/mozart.html

from PIL import Image

with Image.open('mozart.gif') as image:
    width, height = image.size
    pixels = list(image.getdata())
    pink_index = int(*[color[1] for color in image.getcolors() if color[0] != 0 and color[0]%height==0])
    
    for y in range(height):
        col = pixels[(h:=width*y):h+width]
        i = col.index(pink_index)
        col = col[i:] + col[:i]
        for x in range(width):
            image.putpixel((x,y), col[x])
    
    image.show() # romance
    image.save('romance.gif')

    