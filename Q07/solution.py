# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

with Image.open('oxygen.png') as image:
    width, height = image.size

    pixels = list(image.getdata())
    pixel_matrix = [pixels[i * width:(i + 1) * width] for i in range(height)]
    
    pixels_ascii = []
    for i in range(0,width,7):
        pixel=pixel_matrix[height//2][i]
        if pixel[0]==pixel[1]==pixel[2]:
            pixels_ascii+=chr(pixel[0])

    print(''.join(pixels_ascii))
    # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    
    print(''.join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121])))
