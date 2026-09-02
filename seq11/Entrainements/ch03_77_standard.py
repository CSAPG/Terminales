#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 3 Activité 3                                       STANDARD 
# ====================================================================
import matplotlib.pyplot as plt
import numpy as np

# Conductivité molaire ionique
lambda_1=34.98e-3  # Ions oxonium (en S.m²/mol)
lambda_2=7.63e-3   # Ions chlorure (en S.m²/mol)

# ====================================================================
# Etape 1 : Importation des données expérimentales
# ====================================================================

t,sigma=[0],[0]  # Initialisation des listes pour t et la conductivité
with open('C03_act3_data.txt') as fichier:
    header = [fichier.readline() for i in range(2)]
    line = fichier.readline().replace(',','.')
    while line:
        data0,data1=line.split('\t') 
        t.append(float(data0))      # Dates (en s)
        sigma.append(float(data1))  # Conductivité (en S.m²/mol) 
        line=fichier.readline().replace(',','.')
        
# ====================================================================
#  Etape 2 : Calcul des concentrations cB (en mol/L)
# ====================================================================

c0=3.615e-2 # concentration initiale du réactif (en mol/L)
N = len(t)  # Nombre de dates

# Calcul des concentrations cBi en réactif aux dates ti
cB=[c0] # Initialisation de la liste cB des concentrations en réactif par c0 à t=0s
for i in range(1,N,1) : 
    cBi=c0*(1-sigma[i]/sigma[-1]) # Concentration cBi (en mol/L)
    cB.append(cBi) 

# ====================================================================
# Etape 3 : Calcul de la vitesse volumique de consommation de B
# ====================================================================

vB=[] # Définition d'une liste vide pour la vitesse de consommation de B
for i in range(N-1) : 
    vBi=...à compléter...              # vitesse de consommation de B
                                       # (en mol/L/s)  
    vB.append(vBi) 
    
# ====================================================================
# Etape 4 : Représentations graphiques
# ====================================================================
plt.figure(figsize=(12,12))
""" La figure présentera 4 graphes (subplot) sur 2 lignes et 2 colonnes :
plt.subplot(nb de lignes, nb de colonnes, index du graphe)."""
# ====================================================================
plt.subplot(2,2,1)  # Nuage de points [B] = f(t)

plt.plot(t,cB,'+',label='$[B]=f(t)$',clip_on=False)  # Trace le nuage de points de coordonnées (t,cB) légendé '[B]=f(t)'          
plt.xlabel("$t$ (en s)")                             # Label de l'axe des abscisses
plt.ylabel("$[B]$ (en mol$\cdot$L$^{-1}$)")          # Label de l'axe des ordonnées
plt.xlim(0,max(t))                                   # Bornes de l'axe des abscisses
plt.ylim(0,max(cB))                                  # Bornes de l'axe des ordonnées
plt.grid(ls='--')                                    # Grille en pointillés 
plt.legend(loc=9)                                    # Légende centrée en haut                  

# ====================================================================
plt.subplot(2,2,3)  # Nuage de points vB = f(t)

del t[-1]           # Retire la dernière valeur de la liste t
...à compléter...   # Trace le nuage de points de coordonnées (t,vB) légendé 'v_(C,B)=f(t)'
...à compléter...   # Label de l'axe des abscisses    
...à compléter...   # Label de l'axe des ordonnées
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0)) # Ecriture scientifique sur l'axe des ordonnées            
...à compléter...   # Bornes de l'axe des abscisses
...à compléter...   # Bornes de l'axe des ordonnées
...à compléter...   # Grille en pointillés                   
...à compléter...   # Légende centrée en haut                  

# ====================================================================
plt.subplot(2,2,2)  # Nuage de points vB = f([B])

...à compléter...   # Retire la dernière valeur de la liste cB
c_B=np.array(cB)    # Convertit la <liste> 'cB' en <tableau à 1D> 'c_B'

a_1,b_1=np.polyfit(c_B,vB,1) # Modélisation du nuage de points de coordonnées (c_B,vB)
                             # par une droite d'équation  y = a_1*x + b_1
...à compléter...   # Trace le nuage de points de coordonnées (c_B,vB) légendé 'v_(C,B)=f([B])'
plt.plot(c_B,a_1*c_B+b_1,'r',label='Modélisation') # Trace la droite de la modélisation légendée 'Modélisation'

"""
Mettre en forme la fenêtre graphique :
- labels et bornes des axes,
- écriture scientifique sur les 2 axes (axis='both'),
- grille en pointillés et légende centrée en haut.
"""

# ====================================================================
plt.subplot(2,2,4)  # Nuage de points vB = f([B]²)

a_2,b_2=...à compléter... # Modélisation du nuage de points de coordonnées (c_B²,vB)
                          # par une droite d'équation  y = a_2*x + b_2
...à compléter...   # Trace le nuage de points de coordonnées (c_B²,vB) légendé 'v_(C,B)=f([B]²)'
...à compléter...   # Trace la droite de la modélisation légendée 'Modélisation'

"""
Mettre en forme la fenêtre graphique :
- labels et bornes des axes,
- écriture scientifique sur les 2 axes,
- grille en pointillés et légende centrée en haut.
"""

plt.tight_layout()
plt.show()

