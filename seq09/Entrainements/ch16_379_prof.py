#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# =============================================================================

# Chapitre 16 Ex 47                                                  Correction

# =============================================================================

import numpy as np

import matplotlib.pyplot as plt



# Valeurs expérimentales de la capacité calorifique du fer en J.Kg^-1.K^-1

c_fer = [408,494,423,432,439,464,477,467,471,445,471,458,455,445,457,442,448] 



# Affichage de l'histogramme

plt.hist(c_fer, range=(400,500), bins=5, color='blue', edgecolor='black')

plt.title('Histogramme des mesures de la capacité calorifique du fer')

plt.xlabel('Capacité calorifique du fer (en J$\cdot$Kg$^{-1}\cdot$K$^{-1}$)')

plt.ylabel('Effectif')

plt.show()



# Traitement statistique de la série de mesures à l'aide des fonctions NumPy

N=len(c_fer) # Nombre de mesures



Moy_c_fer=np.mean(c_fer)     # Valeur moyenne de c_fer en J.Kg^-1.K^-1

u_c_fer_barre=np.std(c_fer,ddof=1)/N**0.5 # Incertitude-type en J.Kg^-1.K^-1

"""

Remarque : les deux lignes précédentes sont équivalentes à :

Moy_c_fer=sum(c_fer)/N

u_c_fer=(1/(n-1)*sum((np.array(c_fer)-Moy_c_fer)**2.))**0.5/N**0.5

"""



# Affichage brut

print('\n')

print('Capacité calorifique du fer : c_fer = ',Moy_c_fer,'J.Kg^-1.K^-1' )

print('Incertitude-type : u(c_fer_barre) = ',u_c_fer_barre,'J.Kg^-1.K^-1')



# Affichage du résultat de la mesure

print('\n')

print('Le résultat de la mesure est :')

print('c_fer =','%.0f'%Moy_c_fer,'J.Kg^-1.K^-1 avec une incertitude ',

      'u(c_fer_barre) =','%.0f'%u_c_fer_barre,'J.Kg^-1.K^-1' ) 