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
## Defining the Image
The following function is needed in order to identify the picture being resized
```
image = io.imread("https://media.istockphoto.com/id/481526876/photo/boreal-owl-in-autumn-leaves.jpg?s=612x612&w=0&k=20&c=O4orVHRvpFKn77dT86tXn3gA90j3Ig5rMTox-3FBi74=")
```
## Resizing the Image
The following function resizes the image to a scale of 224 x 224 x 3
```
resized_image = resize(cropped_image, (224, 224))
```
This function plots the new cropped image
```
plt.imshow(cropped_image, cmap='gray')
plt.axis('off')  # Hide axes
plt.show()
```
![Unknown-2](https://github.com/Carlbronge/Imagery/assets/143009718/62c3170b-c138-4a0f-aef1-959daf7f57a3)

## Showing a Grey Scale Copy of the Resized Image
The follwoing function turns the cropped image from a RGB color scale to a grey color scale
```
gray_image = color.rgb2gray(resized_image)
```
This function plots the new grey scale cropped image
```
plt.imshow(gray_image, cmap='gray')
plt.axis('off')  # Hide axes
plt.show()
```
![Unknown-3](https://github.com/Carlbronge/Imagery/assets/143009718/75a292a0-02c0-4daa-b054-43b50737d200)

This function shows the shape of the grey scale image
```
gray_image.shape
```
(224, 224)
