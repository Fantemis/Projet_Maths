# -*- coding: utf-8 -*-
from skimage import io
from math import log10
from copy import deepcopy
import bruit_poivre_sel
image = io.imread('Lenna.png', as_grey = True)
image2 = deepcopy(image)
psignal = 0
pbruit = 0
i=0
abs = 0
ord = 0
abs2=0
ord2=0
v=0
moy=0
#Taille de l'image
taille = image.shape[0]

#BRUITAGE
bruit_poivre_sel.bruitage(image)

#DEBRUITAGE1
for i in range(0, image.size):
    while abs < taille-1: 
        v=0
        for ord in range(0, taille-1):
            if image[abs][ord]== 0  or image[abs][ord] == 1 :
                if abs == 0 and ord != 0 and ord != taille:
                    ord2 = ord+1
                    v=v+image[abs2][ord2]
                    abs2=abs+1
                    v=v+image[abs2][ord2]
                    ord2 = ord2-1
                    v=v+image[abs2][ord2]
                    ord2 = ord2-1
                    v=v+image[abs2][ord2]
                    abs2 = abs2-1
                    v=v+image[abs2][ord2]
                    moy=v/5
                    image[abs][ord]=moy
                    v=0  
                    
                elif ord == 0 and abs != 0 and abs != taille:
                    abs2=abs-1
                    v=v+image[abs2][ord2]
                    ord2 = ord+1
                    v=v+image[abs2][ord2]
                    abs2=abs2+1
                    v=v+image[abs2][ord2]
                    abs2=abs2+1
                    v=v+image[abs2][ord2]
                    ord2 = ord2-1
                    v=v+image[abs2][ord2]
                    moy=v/5
                    image[abs][ord]=moy
                    v=0
                elif abs == taille and ord != 0 and ord != taille:
                    ord2 = ord+1
                    v=v+image[abs2][ord2]
                    abs2=abs-1
                    v=v+image[abs2][ord2]
                    ord2 = ord2-1
                    v=v+image[abs2][ord2]
                    ord2 = ord2-1
                    v=v+image[abs2][ord2]
                    abs2 = abs2+1
                    v=v+image[abs2][ord2]
                    moy=v/5
                    image[abs][ord]=moy
                    v=0
                elif ord == taille and abs != 0 and abs != taille:
                    abs2=abs-1
                    v=v+image[abs2][ord2]
                    ord2 = ord-1
                    v=v+image[abs2][ord2]
                    abs2=abs2+1
                    v=v+image[abs2][ord2]
                    abs2=abs2+1
                    v=v+image[abs2][ord2]
                    ord2 = ord2+1
                    v=v+image[abs2][ord2]
                    moy=v/5
                    image[abs][ord]=moy
                    v=0
                elif abs == 0 and ord == taille:
                    abs2=abs+1
                    v=v+image[abs2][ord2]
                    ord2 = ord-1
                    v=v+image[abs2][ord2]
                    abs2=abs2-1
                    v=v+image[abs2][ord2]
                    moy=v/3
                    image[abs][ord]=moy
                    v=0
                elif abs == 0 and ord == 0:
                    abs2=abs+1
                    v=v+image[abs2][ord2]
                    ord2 = ord+1
                    v=v+image[abs2][ord2]
                    abs2=abs2-1
                    v=v+image[abs2][ord2]
                    moy=v/3
                    image[abs][ord]=moy
                    v=0
                elif abs == taille and ord == 0:
                    abs2=abs-1
                    v=v+image[abs2][ord2]
                    ord2 = ord+1
                    v=v+image[abs2][ord2]
                    abs2=abs2+1
                    v=v+image[abs2][ord2]
                    moy=v/3
                    image[abs][ord]=moy
                    v=0
                elif abs == taille and ord == taille:
                    abs2=abs-1
                    v=v+image[abs2][ord2]
                    ord2 = ord-1
                    v=v+image[abs2][ord2]
                    abs2=abs2+1
                    v=v+image[abs2][ord2]
                    moy=v/3
                    image[abs][ord]=moy
                    v=0
                else:
                    abs2=abs-1
                    ord2=ord-1
                    v=v+image[abs2][ord2]
                    abs2 = abs2+1
                    v=v+image[abs2][ord2]
                    abs2 = abs2+1
                    v=v+image[abs2][ord2]
                    ord2=ord2+1
                    v=v+image[abs2][ord2]
                    ord2=ord2+1
                    v=v+image[abs2][ord2]
                    abs2 = abs2-1
                    v=v+image[abs2][ord2]
                    abs2 = abs2-1
                    v=v+image[abs2][ord2]
                    ord2=ord2-1
                    v=v+image[abs2][ord2]
                    #Moyenne
                    moy=v/8
                    image[abs][ord] = moy
                    v=0
        abs=abs+1    
#SNR
for abs in range(0, taille):
    for ord in range(0, taille):
        psignal=psignal+(image2[abs][ord])**2
        pbruit=pbruit+(image2[abs][ord]-image[abs][ord])**2
snr = 10*log10(psignal/pbruit)
io.imshow(image)


#snr = image originale / image debruitée
