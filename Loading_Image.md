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
## Loading The Image
The following python function uses matplotlib library to display a 2D arrary or matrix as an image
```
def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x, cmap = 'gray')
    ax.axis('off')
    fig.set_size_inches(5, 5)
    plt.show()
```
The follwoing function plots the image
```
image = io.imread("https://media.istockphoto.com/id/481526876/photo/boreal-owl-in-autumn-leaves.jpg?s=612x612&w=0&k=20&c=O4orVHRvpFKn77dT86tXn3gA90j3Ig5rMTox-3FBi74=")

image = image[:,:,:]

plot(image)
![Unknown](https://github.com/Carlbronge/Imagery/assets/143009718/db74a449-fefb-4eb5-90e3-2bd97c035de6)


