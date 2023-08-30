# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image
from functools import reduce

lengths = reduce(lambda x, y: x + y, [[i,i-1,i-1,i-2] for i in range(100,0,-2)])

with Image.open('wire.png') as image:
    pixels = list(image.getdata())
    img = Image.new('RGB', (100, 100))
    pos = [-1,0]
    _l = p = 0
    for l in lengths:
        for i in range(l):
            pos[p%2]+= 1 if p<2 else -1
            img.putpixel(pos,pixels[_l+i])
            
        _l+=l
        p=(p+1)%4
            
    img.show() # a cat photo 
    img.save('cat.png')
