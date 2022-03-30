import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

img_1 = Image.open("b.png")
img_2 = np.fft.fft2(img_1)
plt.plot(img_2)
plt.show()
