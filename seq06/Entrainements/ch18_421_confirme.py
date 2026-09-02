#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 18 Activité 6                                      CONFIRME
# ====================================================================
import numpy as np

# Listes L=[valeur,incertitude-type] en unité SI
i=[...,...] # interfrange (en m)
a=[...,...] # Distance entre les centres des fentes (en m)
D=[...,...] # Distance fentes/écran (en m) 

def Alea(L): # Tirage aléatoire selon la loi normale
    return np.random.normal(L[0],L[1])

d=[] # Simulation d'une distribution d pour Lambda
Iteration=100000
for j in range(Iteration) :
    Alea_Lambda=Alea(i)*Alea(a)/(Alea(D))
    d.append(Alea_Lambda*1e9) # Conversion en nm
    
# Calcul de Lambda et de l'incertitude-type u(Lambda)
Lambda=np.mean(d)         # Lambda <- valeur moyenne de d
u_Lambda=np.std(d,ddof=1) # u(Lambda) <- Ecart-type de d

print('\nLongueur d\'onde Lambda =',Lambda,' nm')
print('Incertitude-type : u(Lambda) =',u_Lambda,' nm')

# ====================================================================
# Affichage de l'histogramme de la distribution simulée pour Lambda
from matplotlib import pyplot as plt

"""
Afficher l'histogramme (50 classes) de la distribution d et mettre en
forme la fenêtre graphique (titre, label des axes).
"""

# ====================================================================
# Calcul de Lambda et u(Lambda) par une méthode analytique

def q(L): # avec L=[valeur X,incertitude-type u(X)] en unité SI
    """Renvoie (u(X)/X)**2 pour une grandeur X"""
    return ... A compléter ...

Lambda_1 = ... A compléter ...  # Valeur de Lambda (en nm)
u_Lambda_1=... A compléter ...  # u(Lambda) (en nm)

print('\nMéthode analytique :')
print('Longueur d\'onde Lambda =',Lambda_1,' nm')
print('Incertitude-type : u(Lambda) =',u_Lambda_1,' nm')






