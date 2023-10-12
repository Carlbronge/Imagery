## Installing
These are the required downloads prior to running the following program
```
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from scipy.signal import convolve2d
from skimage import data, color, io
import IPython
import cv2

import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision import datasets
from skimage.util import montage
!pip install wandb
import wandb as wb
from skimage.io import imread
from skimage.transform import resize
from skimage import io, color
from scipy.signal import convolve2d
```
```
import imageio as io
```
## Loading the Image
This command loads the image in grey scale and then plots it
```
image = io.imread("https://media.istockphoto.com/id/481526876/photo/boreal-owl-in-autumn-leaves.jpg?s=612x612&w=0&k=20&c=O4orVHRvpFKn77dT86tXn3gA90j3Ig5rMTox-3FBi74=")
image = image[:,:,0]
image = image.astype(float)
image /= 255.0
plot(image)
```
![Unknown-4](https://github.com/Carlbronge/Imagery/assets/143009718/4e984999-c9e5-4858-926c-848eb6e2d75c)

## Convolving the Image
This function will return a list containing 3 random 5x5 matrices where each matrix will be filled with random numbers drawn from the standard normal distribution
```
def generate_random_filters(num_filters, size):
    return [np.random.randn(size, size) for _ in range(num_filters)]
```
This function takes an input image and a list of filters and returns a list of 2D arrays where each array is the result of convolving the input image with one of the filters from the list.
```
def convolve_with_filters(image, filters):
    return [convolve2d(image, filt, mode='valid') for filt in filters]
```
n = 3
```
