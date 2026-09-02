#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Chapitre 16 Ex 47                                                      Enonce
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

# Valeurs expérimentales de la capacité calorifique du fer en J.Kg^-1.K^-1
c_fer = [408,494,423,432,439,464,477,467,471,445,471,458,455,445,457,442,448] 

plt.hist(c_fer, range=(400,500), bins=5, color='blue', edgecolor='black')
plt.title('Histogramme des mesures de la capacité calorifique du fer')
plt.xlabel('Capacité calorifique du fer (en J$\cdot$Kg$^{-1}\cdot$K$^{-1}$)')
plt.ylabel('Effectif')
plt.show()

N=len(c_fer)
Moy_c_fer=np.mean(c_fer)     
u_c_fer_barre=np.std(c_fer,ddof=1)/N**0.5 

print('\nCapacité calorifique du fer : c_fer = ',Moy_c_fer,'J.Kg^-1.K^-1' )
print('Incertitude-type : u(c_fer_barre) = ',u_c_fer_barre,'J.Kg^-1.K^-1')

