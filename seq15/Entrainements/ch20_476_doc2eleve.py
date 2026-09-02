#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 20 Exercice 35                                       Enoncé
# ====================================================================
from matplotlib import pyplot as plt

import numpy as np
e=1.602176634e-19 # Charge élémentaire (en C)
c=299792458       # Vitesse de la lumière (en m/s)

# Listes L=[valeur,incertitude-type] en unités SI
Us=[...,...]     # Tension de seuil (en V)
Lambda=[...,...] # Longueur d'onde (en m)

def Alea(L): # Tirage aléatoire selon la loi normale
    return np.random.normal(L[0],L[1])

# Simulation d'une distribution d pour h
d=[]
Iteration=100000
for j in range(Iteration):
    Alea_h=e*Alea(Us)*Alea(Lambda)/c
    d.append(Alea_h)

# Calcul de h et de l'incertitude-type u(h)
h=...A compléter...          # h <- valeur moyenne de d
u_h=...A compléter...   # u(h) <- écart-type de d

#Affichage
print('Constante de Planck h :', h,' J.s')
print('Incertitude-type u(h) :',u_h,' J.s')

plt.hist(d, bins = 50, color = 'blue', edgecolor ='black')
plt.xlabel('h')
plt.ylabel('effectif')
plt.title('Pour %i' %Iteration +' iterations')
plt.show()