import numpy as np
from PIL import Image
import math
import time
import multiprocessing

start_time = time.time()


print(multiprocessing.cpu_count())

imgH = 1440
imgW = 2560

colors = []
print("Checpoint 0: --- %s seconds ---" % (time.time() - start_time))

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
print("Checpoint 1: --- %s seconds ---" % (time.time() - start_time))

colors = bytes(colors)
print("Checpoint 2: --- %s seconds ---" % (time.time() - start_time))
img = Image.frombytes('RGB', (imgW, imgH), colors)
print("Checpoint 3: --- %s seconds ---" % (time.time() - start_time))
img.show()
print("Checpoint 4: --- %s seconds ---" % (time.time() - start_time))
img.save('out/current.png')
print("Checpoint 5: --- %s seconds ---" % (time.time() - start_time))
