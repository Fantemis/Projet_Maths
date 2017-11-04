#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import bruit_multiplicatif
import filtrage_median
from skimage import io
import matplotlib.pyplot as plt
from math import log10
from copy import deepcopy

image = io.imread('lena.jpg', dtype = float)
image2 = deepcopy(image)

#Taille de l'image
taille = image.shape[0]
abs = 0
ord = 0
pbruit = 0
psignal = 0

#----------------BRUITAGE---------------------
bruit_multiplicatif.bruit(image)


#-------------DEBRUITAGE----------------------
filtrage_median.debruit(image)

#SNR
for abs in range(0, taille):
    for ord in range(0, taille):
        psignal=psignal+(image2[abs][ord])**2
        pbruit=pbruit+(image2[abs][ord]-image[abs][ord])**2
snr = 10*log10(psignal/pbruit)
plt.imshow(image, cmap="gray")
plt.colorbar()