#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 18 Activité 6                                    CORRECTION
# ====================================================================
import numpy as np

# Définition des listes  L = [valeur,incertitude-type] en unité SI
i=[6.4e-3,0.05e-3]  # interfrange (en m)
a=[0.2e-3,0.02e-3]  # Distance entre les centres des fentes (en m)
D=[2,0.5e-3]        # Distance fentes/écran (en m) 

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
plt.hist(d,bins=50,color='blue',edgecolor='black')
plt.xlabel('$\lambda$ (en nm)')
plt.ylabel('Effectif')
plt.title('Pour %d'%Iteration+ ' itérations')
plt.show()

# ====================================================================
# Calcul de Lambda et u(Lambda) par une méthode analytique

def q(L): # avec L=[valeur X,incertitude-type u(X)] en unité SI
    """Renvoie (u(X)/X)**2 pour une grandeur X"""
    return (L[1]/L[0])**2

Lambda_1 = (i[0]*a[0]/D[0])*1e9           # Valeur de Lambda (en nm)
u_Lambda_1=Lambda_1*(q(i)+q(a)+q(D))**0.5 # u(Lambda) (en nm)

print('\nMéthode analytique :')
print('Longueur d\'onde Lambda =',Lambda_1,' nm')
print('Incertitude-type : u(Lambda) =',u_Lambda_1,' nm')






