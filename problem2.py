# -*- coding: utf-8 -*-
"""Problem2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cc3LqMqYdYlpcH1pjryIVNPsvtxMOFqy
"""

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

import imageio as io

def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x, cmap = 'gray')
    ax.axis('off')
    fig.set_size_inches(5, 5)
    plt.show()

image = io.imread("https://media.istockphoto.com/id/481526876/photo/boreal-owl-in-autumn-leaves.jpg?s=612x612&w=0&k=20&c=O4orVHRvpFKn77dT86tXn3gA90j3Ig5rMTox-3FBi74=")

image = image[:,:,:]

plot(image)

image.shape

image = io.imread("https://media.istockphoto.com/id/481526876/photo/boreal-owl-in-autumn-leaves.jpg?s=612x612&w=0&k=20&c=O4orVHRvpFKn77dT86tXn3gA90j3Ig5rMTox-3FBi74=")

resized_image = resize(cropped_image, (224, 224))

plt.imshow(cropped_image, cmap='gray')
plt.axis('off')  # Hide axes
plt.show()

resized_image.shape

gray_image = color.rgb2gray(resized_image)

plt.imshow(gray_image, cmap='gray')
plt.axis('off')  # Hide axes
plt.show()

gray_image.shape

image = io.imread("https://media.istockphoto.com/id/481526876/photo/boreal-owl-in-autumn-leaves.jpg?s=612x612&w=0&k=20&c=O4orVHRvpFKn77dT86tXn3gA90j3Ig5rMTox-3FBi74=")
image = image[:,:,0]
image = image.astype(float)
image /= 255.0
plot(image)

def generate_random_filters(num_filters, size):
    return [np.random.randn(size, size) for _ in range(num_filters)]

def convolve_with_filters(image, filters):
    return [convolve2d(image, filt, mode='valid') for filt in filters]

n = 3

filters = generate_random_filters(10, n)

feature_maps = convolve_with_filters(image, filters)

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