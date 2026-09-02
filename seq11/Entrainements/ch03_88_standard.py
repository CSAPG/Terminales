#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 3 Exercice 29                                    Correction 
# ====================================================================
import matplotlib.pyplot as plt

"""
Les données expérimentales sont stockées dans les variables :
  - t : liste des dates ti (en s)
  - V_gaz : liste du volume total de gaz formé aux dates ti (en m^3)
"""
n_0=0.01  # Quantité initiale de chlorure de sulfuryle (en mol)
V_0=0.1   # Volume du mélange réactionnel (en L)
p=float(input("Pression ambiante (en Pa) : p = "))
T=float(input("Température ambiante (en K) : T = "))
V_m=8.314*T/p  # Volume molaire (en m^3)

N=len(t)
# Liste de la concentration en réactif aux dates ti
c_r=[(n_0/V_0)-V_gaz[i]/(2*V_m*V_0) for i in range(N)]

# Liste de la vitesse de consommation du réactif aux dates ti
v_r=[... A compléter... for i in range(N-1)] 

del t[-1]
plt.plot(t,v_r,'+') #  Représentation graphique v_r=f(t)
plt.xlabel("$t$ (en s)")              
plt.ylabel(...A completer...)
plt.show()

