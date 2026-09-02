#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 18 Exercice 21                                       ENONCE
# ====================================================================
from matplotlib import pyplot as plt
from math import pi
import numpy as np

T=1 # en milliseconde
t=np.linspace(0,4,400)
A1=float(input('Amplitude du signal 1 (en mV) : A1 ='))
A2=float(input('Amplitude du signal 2 (en mV): A2 ='))
phi=eval(input('Phase à l\'origine (en rad): phi ='))

def s(A,T,phi):
    return A*np.cos(2*pi*t/T+phi)

plt.plot(t,s(A1,T,0),'--',lw=1.2,label='$s_{1}(t)$')
plt.plot(t,s(A2,T,phi),'--',lw=1.2,label='$s_{2}(t)$')
plt.plot(t,s(A1,T,0)+s(A2,T,phi),lw=2.5,label='$s_{1}(t)+ s_{2}(t)$')

plt.title('Somme de deux signaux sinusoïdaux')
plt.xlim(0,4)
plt.ylim(-1.5*(A1+A2),1.5*(A1+A2))
plt.xlabel('$t$ (en s)')
plt.ylabel('Elongation (en mV)')
plt.grid(which='both',ls='--')
plt.legend(loc=9, ncol=3)
plt.show()


