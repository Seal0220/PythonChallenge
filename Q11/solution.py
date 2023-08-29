# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

with Image.open('cave.jpg') as image:
    width, height = image.size

    pixels = list(image.getdata())
    pixel_odd, pixel_even = [], []
    for i in range(len(pixels)):
        if i%2 == 0:
            pixel_even.append(pixels[i])
        elif i%2 == 1:
            pixel_odd.append(pixels[i])
            
    def createImage(pixels):
        img = Image.new('RGB', (width//2, height//2))
        for y in range(height//2):
            for x in range(width//2):
                pixel_index = y * width + x
                pixel_color = pixels[pixel_index]
                img.putpixel((x, y), pixel_color)
        return img
        
    pixel_even_image = createImage(pixel_even)
    pixel_odd_image = createImage(pixel_odd)
    
    pixel_even_image.show()
    pixel_even_image.save('even.jpg')
    
    pixel_odd_image.show()
    pixel_odd_image.save('odd.jpg')