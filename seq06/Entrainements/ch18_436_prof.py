#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 18 Exercice 41                                   CORRECTION
# ====================================================================
from matplotlib import pyplot as plt
from math import pi
import numpy as np

T=0.5  # Période en ms
A1=2 # Amplitude de s1 en mV
A2=5 # Amplitude de s2 en mV

# Saisie par l'utilisateur de la phase à l'origine du signal s2(t)
phi=eval(input("Phase à l'origine de s2(t) (entre -2*pi et 2*pi) : phi = "))
t=np.linspace(0,15,800)  # Définition du tableau des dates en ms

# Définition des tableaux des ordonnées de la forme s(t)=A*cos(2πt/T + phi)
s1=A1*np.cos(2*pi*t/T)
s2=A2*np.cos(2*pi*t/T+phi)
s=s1+s2

# Définition de la figure contenant 2 graphes répartis sur '1 ligne,2 colonnes'
figure=plt.subplots(1,2)

# Graphe 1 de gauche
plt.subplot(1,2,1)
plt.plot(t,s1,'b',label='$s_{1}(t)$')
plt.plot(t,s2,'r',label='$s_{2}(t)$')
plt.xlim(0,1.5)
A=A1+A2
plt.ylim(-1.5*A,1.5*A)
plt.title("Signaux à ajouter ")
plt.xlabel("$t$ (en ms)")
plt.ylabel("Elongation (en mV)")
plt.grid()
plt.legend()

# Graphe 2 de droite
plt.subplot(1,2,2)
plt.plot(t,s,'g',label='$s_{3}(t)$')
plt.xlim(0,1.5)
plt.tick_params(axis='y',left=False,right=True,
                labelleft=False,labelright=True)
plt.ylim(-1.5*A,1.5*A)
plt.title("Somme des signaux")
plt.xlabel("$t$ (en ms)")
plt.ylabel("Elongation (en mV)")
plt.grid()
plt.legend(loc='upper left')

plt.show()





