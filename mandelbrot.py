from PIL import Image, ImageDraw
w = 600
h = 400
im = Image.new('RGB', (w, h), (0, 0, 0))
draw = ImageDraw.Draw(im)
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 100:
        z = z*z + c
        n += 1
    return n
for x in range(w):
    for y in range(h):
        c = complex(-2 + (x / w) * 3, -1 + (y / h) * 2)
        c = 255 - int(mandelbrot(c) * 255 / 100)
        draw.point([x, y], (c, c, c))
im.save('mandelbrot.png')
