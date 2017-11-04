#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
image = io.imread('lena.jpg', dtype = float)


#----------------BRUITAGE---------------------
def bruit(image):
    #Taille de l'image
    taille = image.shape[0]
    sigma = 25
    n=np.random.randn(image.shape[0], image.shape[1])
    for abs in range(0, taille): 
        for ord in range(0, taille):  
            image[abs][ord] = image[abs][ord]+sigma*n[abs][ord]
            if((image[abs][ord]) < 0):
                image[abs][ord]= 0
            elif((image[abs][ord])> 255):
                image[abs][ord]= 255
bruit(image)
plt.imshow(image, cmap="gray")
plt.colorbar()