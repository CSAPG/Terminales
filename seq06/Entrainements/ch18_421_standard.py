#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 18 Activité 6                                      STANDARD
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





























