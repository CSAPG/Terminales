#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Chapitre 12 Exercice 39  Vers le supérieur                        Correction
# Mouvement d'un volant de badminton 
# =============================================================================
import matplotlib.pyplot as plt
from math import pi, cos, sin, sqrt

g = 9.8    # Intensité de la pesanteur en N/kg
m = 5e-3   # Masse du volant en kg
v0 = 50    # valeur de la vitesse initiale en m/s
alpha = 55 # angle de tir    
z0 = 5   # altitude initiale en m

# Initialisation
t=0
z=z0
x=0
vx=v0*cos(alpha/180*pi)
vz=v0*sin(alpha/180*pi)
ec=0.5*m*v0**2
epp=m*g*z0
em=ec+epp
# Création des différentes listes vides
T,X,Z=[t],[x],[z]
Vx,Vz=[vx],[vz]
Ec,Epp,Em=[ec],[epp],[em]

dt = 50e-3  # choix du pas d'itération en s
while z>0:
    dx=vx*dt
    dz=vz*dt
    dvx=-0.15*sqrt(vx**2+vz**2)*vx*dt
    dvz=-9.8*dt-0.15*sqrt(vx**2+vz**2)*vz*dt
    t=t+dt
    x=x+dx
    z=z+dz
    vx=vx+dvx
    vz=vz+dvz
    ec=......................
    epp........................
    em=...................
    T.append(t)
    Vx.append(vx), Vz.append(vz)
    X.append(x), Z.append(z)
    Ec.append(ec), Epp.append(epp), Em.append(em)

fig,(traj,Energie)=plt.subplots(1,2)
fig.subplots_adjust(wspace=0.4)

..........................................  # Tracé de la trajectoire
............................................# Définition du titre du graphique et des titres des axes        
xMin,xMax=traj.get_xlim()
traj.set_xlim(0,xMax)
yMin,yMax=traj.get_ylim()
traj.set_ylim(0,yMax)
traj.grid() 


...........................................# Tracé de la courbe donnant l'évolution de l'énerrgie potentielle de pesanteur
...........................................# Tracé de la courbe donnant l'évolution de l'énerrgie cinétique
...........................................# Tracé de la courbe donnant l'évolution de l'énerrgie mécanique
...........................................# Définition du titre du graphique et des titres des axes       
xMin,xMax=Energie.get_xlim()
Energie.set_xlim(0,xMax)
yMin,yMax=Energie.get_ylim()
Energie.set_ylim(0,yMax)
Energie.grid()
Energie.legend()

plt.show() 


