from PIL import Image

image = Image.open('./oxygen.png').convert('L')
grayscaleRectangle = image.crop((0, 45, 607, 50))
grayscaleNumValues = list(grayscaleRectangle.getdata())

grayscaleparsed = grayscaleNumValues[0::7]

#[print("".join(chr(element)), end='') for element in grayscaleparsed ]

nextLevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]

[print("".join(chr(element)), end='') for element in nextLevel ]
