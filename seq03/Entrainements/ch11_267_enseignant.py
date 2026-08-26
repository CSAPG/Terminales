#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 11 Exercice 40                                   CORRECTION
# ====================================================================
import numpy as np
from matplotlib import pyplot as plt
from math import *
#-----Génération des coordonnées du projectile ---------------------
t =np.linspace(0.0,3,11)    # Définition du domaine des dates (en s)
x = 10.0*t                  # Définition des abscisses (en m)
y = -4.9*t**2+14.9*t        # Définition des ordonnées (en m)

#-----Figure représentant la trajectoire y=f(x) --------------------
plt.figure('Étude d\'un projectile')
plt.title('Vecteurs vitesse et accélération du projectile')
plt.xlabel('x(en m)')
plt.ylabel('y(en m)')
plt.plot(x,y,'ro',ms=2)
plt.axis('equal')

#-----Calculs des coordonnées des vecteurs vitesse V----------------
# définition de 2 listes pour les variables Vx et Vy
Vx,Vy=[''],[''] # La première valeur de chaque liste est remplie par
                # une espace pour la position 0 non calculable
for i in range(1,10) :
    # Coordonnées Vxi des vecteurs vitesse sur l'axe x au point i
    Vxi=(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
    Vx.append(Vxi)          # ajout de la valeur Vxi à la liste Vx

    # Coordonnées Vyi des vecteurs vitesse sur l'axe y au point i
    Vyi=(y[i+1]-y[i-1])/(t[i+1]-t[i-1])
    Vy.append(Vyi)          # ajout de la valeur Vyi à la liste Vy

#-----Tracé d'un vecteur vitesse sur deux aux points d'indice i---
for i in range(1,10,2) :
    plt.arrow(x[i],y[i],0.25*Vx[i],0.25*Vy[i],width=0.05,
    length_includes_head="true",color='g')

#-----Calculs des coordonnées des vecteurs accélération a------------
# définition de 2 listes pour les variables ax et ay
ax,ay=['',''],['','']   # Les 2 1ères valeurs de chaque liste sont remplies par
                        # des espaces pour les positions 0 et 1 non calculables
for i in range(2,9) :
    # Coordonnées axi des vecteurs accélération sur l'axe x au point i
    axi=(Vx[i+1]-Vx[i-1])/(t[i+1]-t[i-1])
    ax.append(axi)          # ajout de la valeur axi à la liste ax

    # Coordonnées axi des vecteurs accélération sur l'axe y au point i
    ayi=(Vy[i+1]-Vy[i-1])/(t[i+1]-t[i-1])
    ay.append(ayi)          # ajout de la valeur ayi à la liste ay

#-----Tracé d'un vecteur accélération sur deux aux points i
for i in range(2,9,2) :
    plt.arrow(x[i], y[i], 0.25*ax[i],0.25*ay[i],width=0.05,
    length_includes_head="true",color='b')

plt.show()

