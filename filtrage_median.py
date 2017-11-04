#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from numpy import median

def debruit(image):
    #Taille de l'image
    taille = image.shape[0]
    abs = 0
    ord = 0
    abs2 = 0
    ord2 = 0
    liste=[]
    for i in range(0, image.size):
        while abs < taille-1: 
            v=0
            for ord in range(0, taille-1):
                if abs == 0 and ord != 0 and ord != taille:
                    ord2 = ord+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2 = abs2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    liste.sort
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                elif ord == 0 and abs != 0 and abs != taille:
                    abs2=abs-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                elif abs == taille and ord != 0 and ord != taille:
                    ord2 = ord+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2 = abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                elif ord == taille and abs != 0 and abs != taille:
                    abs2=abs-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                elif abs == 0 and ord == taille:
                    abs2=abs+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                elif abs == 0 and ord == 0:
                    abs2=abs+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                elif abs == taille and ord == 0:
                    abs2=abs-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                elif abs == taille and ord == taille:
                    abs2=abs-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2 = ord-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2=abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord]=median(liste)
                    v=0
                    del(liste[:])
                else:
                    abs2=abs-1
                    ord2=ord-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2 = abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2 = abs2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2=ord2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2=ord2+1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2 = abs2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    abs2 = abs2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    ord2=ord2-1
                    v=image[abs2][ord2]
                    liste.append(v)
                    image[abs][ord] = median(liste)
                    v=0
                    del(liste[:])
            abs=abs+1