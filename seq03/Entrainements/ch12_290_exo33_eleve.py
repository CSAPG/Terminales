#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Chapitre 12 Exercice 38                                            Correction 
# =============================================================================
"""
Pour une bonne visualisation des représentations graphiques, il est conseillé
de régler les préférences de la console en mode inline (Outils>>Préférences).
"""
import matplotlib.pyplot as plt
from math import pi, sin, cos
import numpy as np

g = 9.81   # Intensité de la pesanteur en N/kg

v0=float(input("Valeur de la vitesse initiale (en m/s) : v0 = "))
alpha=float(input("Valeur de l'angle de tir (en degré) : alpha = "))

portee=v0**2*sin(2*alpha/180*pi)/g    # calcul de la portée
fleche=v0**2*(sin(alpha/180*pi))**2/(2*g) # calcul de la flèche

print("\nLa portée est égale à :","%.2f m"%portee)
print("La flèche est égale à :","%.2f m"%fleche)

# Tracé des trajectoires pour différentes valeurs de alpha avec v0 choisie
valeursalpha=[20,30,35,45,55,60,70,80] # en degré
for i in valeursalpha:
    tmax=2*v0*sin(i/180*pi)/g   #calcul de la date pour laquelle z = 0
    t=np.linspace(0,tmax,100)
    x=v0*cos(i/180*pi)*t               #calcul de x à la date t
    z=-0.5*g*t**2+v0*sin(i/180*pi)*t   #calcul de z à la date t
    plt.plot(x,z, label = r"$\alpha$=%.0f°"%i)

plt.title(r"Trajectoire selon $\alpha$ pour v$_{0}$= %.1f"%v0+r' m$\cdot$s$^{-1}$')  
plt.xlabel("$x$ ( en m)")              
plt.ylabel("$z$ ( en m)")         
xMin,xMax,yMin,yMax = plt.axis()
plt.xlim(0,xMax)
plt.ylim(0,yMax)
plt.legend()
plt.grid()                    
plt.show()

# Tracé des trajectoires pour différentes valeurs de v0 avec alpha choisi
valeursv0=[5,10,15,20,25] # en m/s
for i in valeursv0:
    tmax=2*i*sin(alpha/180*pi)/g
    t=np.linspace(0,tmax,100)
    x=i*cos(alpha/180*pi)*t
    z=-0.5*g*t**2+i*sin(alpha/180*pi)*t
    plt.plot(x,z,label = r"$v_{0}$=%.0f m$\cdot$s$^{-1}$"%i)

plt.title(r"Trajectoire selon v$_{0}$ pour $\alpha$=%.0f°"%alpha)   
plt.xlabel("$x$ (en m)")              
plt.ylabel("$z$ (en m)")         
xMin,xMax,yMin,yMax = plt.axis()
plt.xlim(0,xMax)
plt.ylim(0,yMax)
plt.legend()
plt.grid()                    
plt.show()
