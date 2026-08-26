#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =====================================================================
# Chapitre 13 Activité 3                                     CORRECTION
# =====================================================================
"""
Ce programme permet de tester la troisème loi de Kepler à partir des
données (demi grand axe et période de révolution) des planètes du
système solaire regroupées dans le fichier Kepler3_data.txt.
"""
# ============ Extraction des données : NE PAS MODIFIER ==============
import numpy as np

with open('Kepler3_data.txt') as fichier:
    header = [fichier.readline() for i in range(5)]
    a=np.array([float(i) for i in fichier.readline().split(';')])
    T=np.array([float(i) for i in fichier.readline().split(';')])

# ============ Programme à compléter =================================

from matplotlib import pyplot as plt

x=a**3
y=T**2

k,b=np.polyfit(x,y,1) # Modélisation par une droite d'équation y=k*x+b

# Affichage du nuage de points et de sa modélisation
plt.plot(x,y,'+',ms=10,label='Données')
plt.plot(x,k*x+b,'r-',label='Modélisation')
plt.xlabel('$a^{3}$ (en $\mathrm{ua}^{3}$)')
plt.ylabel('$T^{2}$ (en $\mathrm{an}^{2}$)')
plt.legend(loc=4)
plt.grid()
plt.show()


# ============ Affichage de l'équation de la modélisation =============

equation=r'$T^{2} =$'+str('%.4f'%k)+r'$\times a^{3}+$'+str('%.4f'%b)
plt.text(0,4*max(y)/5,'Equation de la modélisation :\n'+equation)

# ============ Calcul et affichage de la masse du Soleil ==============
"""
Approximation d'une orbite circulaire : k = 4π^2/(G*M_S).
"""
from math import pi
ua=1.495978707E11   # unité astronomique (en m)
an = 365.25*24*3600 # année terrestre (en s)

k_SI=k*an**2/ua**3  # Conversion de k en unités SI

G=6.673e-11         # Constante de gravitation (en N.m^2.kg^-2)

M_S=4*pi**2/(G*k_SI)#  Calcul de la masse du Soleil (en kg)

print('La masse du Soleil est estimée à M_Soleil =','%.3e' % M_S,'kg')

