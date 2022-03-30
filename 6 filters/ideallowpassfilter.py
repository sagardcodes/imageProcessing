
#filters 
import math
import numpy
import scipy.fftpack as fftim
from PIL import Image

a = Image.open('image.jpg').convert('L')

b = numpy.asarray(a)

c = fftim.fft2(b)

d = fftim.fftshift(c)

# initializing variables
M = d.shape[0]
N = d.shape[1]

H = numpy.ones((M, N))
center1 = M / 2
center2 = N / 2

d_0 = 30.0  # cut_off radius

# order of BLPF
# t1 = 1
# t2 = 2 * t1
# for gaussian
t1 = 2 * d_0

for i in range(1, M):
    for j in range(1, N):
        r1 = (i - center1) ** 2 + (j - center2) ** 2
        # euclidean distancefrom origin
        r = math.sqrt(r1)
        # using cut_off radius to eliminate high freq
        #  if r > d_0:
        # for ideal low pass
        # H[i, j] = 0.0

        # for butterworth low pass
        # H[i, j] = 1 / (1 + (r / d_0) ** t1)
        # for Gaussian low pass
        # H[i, j] = math.exp(-r ** 2 / t1 ** 2)
        if 0 < r < d_0:
            # for ideal high pass
            # H[i, j] = 1.0
            # for butterworth high pass filter
            H[i, j] = 1 / (1 + (d_0 / r) ** t1)
            # for gaussian high pass
            # H[i, j] = 1 - math.exp(-r ** 2 / t1 ** 2)

# converting H to image
H = Image.fromarray(H)
# performing convolution
con = d * H

# computing mag of inverse FFT
e = abs(fftim.ifft2(con))

# from array to image
f = Image.fromarray(e)
Image._showxv(f, "Sagar lowpass filter")
