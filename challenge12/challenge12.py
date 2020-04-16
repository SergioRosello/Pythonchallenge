# This was too much of a strecth
# I had to look this up
data = open("evil2.gfx", "rb").read()
for i in range(5):
    open('%d.jpg' % i, 'wb').write(data[i::5])

# Expanding on the exercise, if you do: file {0..4}.jpg
# you can see the following output.

# 0.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 180x180, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=0], baseline, precision 8, 640x480, components 3
# 1.jpg: PNG image data, 400 x 300, 8-bit/color RGB, non-interlaced
# 2.jpg: GIF image data, version 87a, 320 x 240
# 3.jpg: PNG image data, 320 x 240, 8-bit/color RGB, non-interlaced
# 4.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 180x180, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=0], baseline, precision 8, 640x480, components 3
