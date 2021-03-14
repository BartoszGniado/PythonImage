import numpy as np
from PIL import Image
import math



print(multiprocessing.cpu_count())

imgH = 1440
imgW = 2560

colors = []

for h in range(imgH):
    scaledH = math.floor(255 * h/imgH)
    for w in range(imgW):
        scaledW = math.floor(255 * w/imgW)
        scaledPiW = math.pi * w/imgW
        r =  scaledW
        # r = 255 if w > (imgW /2) else 0
        g = scaledH
        b = math.floor(abs( math.sin(scaledPiW) *255))
        colors.extend([r,g,b])

colors = bytes(colors)
img = Image.frombytes('RGB', (imgW, imgH), colors)
img.show()
img.save('out/current.png')