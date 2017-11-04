# -*- coding: utf-8 -*-
from random import randrange
from skimage import io
image = io.imread('Lenna.png', as_grey = True)


#BRUITAGE
def bruitage(image):
    #Taille de l'image
    taille = image.shape[0]
    size=image.size
    for i in range(0, size):   
        nr = randrange(1.0,10.0)
        if 0.0<=nr<=1.0:
            nc = randrange(0,2) #noir ou blanc
            na = randrange(0,taille-1)#abscises
            no = randrange(0,taille-1)#ordonnées
            if nc == 0:
                image[na][no] = 0
            else:
                image[na][no] = 1
bruitage(image)
io.imshow(image)