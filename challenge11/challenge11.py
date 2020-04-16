from PIL import Image

image = Image.open("./cave.jpg")
(coord_x, coord_y) = image.size

# Creating the new images
odd = Image.new('RGB', (coord_x // 2, coord_y // 2))
even = Image.new('RGB', (coord_x // 2, coord_y // 2))

pixel = ()
for x in range(coord_x):
    for y in range(coord_y):
        pixel = image.getpixel((x, y))
        if (x + y) % 2 == 0:
            even.putpixel((x // 2, y // 2), pixel)
        else:
            odd.putpixel((x // 2, y // 2), pixel)

odd.save("odd.jpeg", format="jpeg")
even.save("even.jpeg", format="jpeg")
