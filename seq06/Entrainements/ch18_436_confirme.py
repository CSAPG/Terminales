#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 18 Exercice 41                                     CONFIRME       
# ====================================================================
from matplotlib import pyplot as plt
from math import pi
import numpy as np

T=1  # Période 
A1=2 # Amplitude de s1
A2=5 # Amplitude de S2

phi=eval(input('Phase à l\'origine de s2(t) : phi = '))
t=np.linspace(0,15,100)

s1=A1*np.cos(2*pi*t/T)
s2=A2*np.cos(2*pi*t/T)
s=s1+s2

# Définition de la figure contenant 2 graphes
# répartis sur '1 ligne , 2 colonnes'
figure=plt.subplots(1,2) 

plt.subplot(1,2,1) # Graphe 1 de gauche
plt.plot(t,s1,"-+",label='$s_{1}(t)$')
plt.plot(t,s2,"-x",label='$s_{2}(t)$')
plt.xlim(0,10)
A=A1+A2
plt.ylim(-1.5*A1,1.5*A1)
plt.ylabel('Amplitude (en mV)')

plt.subplot(1,2,2) # Graphe 2 de droite
plt.plot(t,s,'.-g',label='$s_{3}(t)$')
plt.xlim(0,1.5)
plt.tick_params(axis='y',left=False,right=True,
                labelleft=False,labelright=True)
plt.ylim(-1.5*A,1.5*A)
plt.legend(loc ='upper left')
plt.grid()

plt.show()


