from PIL import Image

im = Image.open("download.png")
width,height=im.size
print(im.getpixel((0, 0)))

for x in range(width):
    for y in range(height):
        current_color = im.getpixel((x,y))
        if current_color == (192,192,192,255) or current_color == (0,0,0,255):
            im.putpixel((x,y), (255,255,255,255))
        else:
            im.putpixel((x,y), (0,0,0,255))
            
im.save('edit',"PNG")
