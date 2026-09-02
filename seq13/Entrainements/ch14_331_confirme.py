#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Chapitre 14 Type Exercice 27                                       Précision  
# =============================================================================
import numpy as np
from matplotlib import pyplot as plt

# Listes L=[valeur,incertitude-type] en unité SI
delta_t=[40.3,0.3]   # durée (en s)
V_burette=[50.0e-6,0.05e-6]  # Volume de la burette en m³

def Alea(L):
    #Tirage entre -infini et +infini (loi normale)
    tirage=np.random.normal()
    return L[0]+L[1]*tirage
  
Dv=[]
Iteration=100000
for i in range(Iteration) :
    Alea_Dv=Alea(V_burette)/(Alea(delta_t))
    Dv.append(Alea_Dv)
    
Moy_Dv=np.mean(Dv)         
u_Dv=np.std(Dv,ddof=1) 

#Affichage brut
#Afficher le débit volumique avec ses unités et l'incertitude associée.


# Affichage de l'histogramme de la distribution simulée pour le débit volumique 
#Définir l'histogramme à afficher, puis l'afficher. Ne pas oublier les unités. 
