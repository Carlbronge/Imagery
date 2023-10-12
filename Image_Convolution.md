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
This is the size of the filters
```
n = 3
```
This is the number of filters being applied along with their height, each will hold 10 random 3x3 matrices with each matrix in the list having values drawn from the standard normal distribution
```
filters = generate_random_filters(10, n)
```
This is a function to call the previously described convolve_with_filters function and it assigns the result to the variable feature maps.
```
feature_maps = convolve_with_filters(image, filters)
```
## Plotting the Image
This is the function that convolves the orignal image into 10 differnt images each having their own feature map plotted side by side
```
plt.figure(figsize=(15, 15))
for i, (filt, feature_map) in enumerate(zip(filters, feature_maps)):
    plt.subplot(10, 2, 2*i+1)
    plt.imshow(filt, cmap="gray")
    plt.title(f"Filter {i+1}")
    plt.axis('off')
    
    plt.subplot(10, 2, 2*i+2)
    plt.imshow(feature_map, cmap="gray")
    plt.title(f"Feature Map {i+1}")
    plt.axis('off')

plt.tight_layout()
plt.show()
```
![Unknown-5](https://github.com/Carlbronge/Imagery/assets/143009718/6c9b352b-e8e6-44c2-883c-ccd03f7b3f7f)

