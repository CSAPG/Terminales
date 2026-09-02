#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 3 Activité 3                                     CORRECTION 
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
    vBi=-(cB[i+1]-cB[i])/(t[i+1]-t[i]) # vitesse de consommation de B
                                       # (en mol/L/s)  
    vB.append(vBi) 
    
# ====================================================================
# Etape 4 : Représentations graphiques
# ====================================================================
plt.figure(figsize=(12,12))
""" La figure présentera 4 graphes (subplot) sur 2 lignes et 2 colonnes :
plt.subplot(nb de lignes, nb de colonnes, index du graphe)."""
# ====================================================================
plt.subplot(2,2,1)      # Nuage de points [B] = f(t)

plt.plot(t,cB,'+', label = '$[B]=f(t)$', clip_on=False)             
plt.xlabel("$t$ (en s)")   
plt.ylabel("$[B]$ (en mol$\cdot$L$^{-1}$)")
plt.xlim(0,max(t))
plt.ylim(0,max(cB))
plt.grid(ls='--')
plt.legend(loc=9)                   

# ====================================================================
plt.subplot(2,2,3)      # Nuage de points vB = f(t)

del t[-1]       # Retire la dernière valeur de la liste t
plt.plot(t,vB,'c+', label = '$v_{C,B}=f(t)$', clip_on=False)
plt.xlabel("$t$ (en s)")   
plt.ylabel("$v_{C,B}$ (en mol$\cdot$L$^{-1}\cdot$s$^{-1}$)")
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))             
plt.xlim(0,max(t))
plt.ylim(0,max(vB))
plt.grid(ls='--')                    
plt.legend(loc=9)                    

# ====================================================================
plt.subplot(2,2,2)      # Nuage de points vB = f([B])

del cB[-1]       # Retire la dernière valeur de la liste cB
c_B=np.array(cB) # Convertit la <liste> 'cB' en <tableau à 1D> 'c_B'

a_1,b_1=np.polyfit(c_B,vB,1) # Modélisation de la forme y = a*x + b

plt.plot(c_B,vB,'b+', label='$v_{C,B}=f([B])$', clip_on=False)
plt.plot(c_B,a_1*c_B+b_1,'r',label='Modélisation')
plt.xlabel("$[B]$ (en mol$\cdot$L$^{-1}$)")
plt.ylabel("$v_{C,B}$ (en mol$\cdot$L$^{-1}\cdot$s$^{-1}$)")
plt.ticklabel_format(axis='both',style='sci',scilimits=(0,0))             
plt.xlim(0,max(c_B))
plt.ylim(0,max(vB))
plt.grid(ls='--') 
plt.legend(loc=9)

# ====================================================================
plt.subplot(2,2,4)      # Nuage de points vB = f([B]²)

a_2,b_2=np.polyfit(c_B**2,vB,1) # Modélisation de la forme y = a*x + b

plt.plot(c_B**2,vB,'b+',label='$v_{C,B}=f([B]^{2})$', clip_on=False)
plt.plot(c_B**2,a_2*(c_B**2)+b_2,'r',label='Modélisation')
plt.xlabel("$[B]^{2}$ (en mol$^{2}\cdot$L$^{-2}$)")             
plt.ylabel("$v_{C,B}$ (en mol$\cdot$L$^{-1}\cdot$s$^{-1}$)")
plt.ticklabel_format(axis='both',style='sci',scilimits=(0,0))             
plt.xlim(0,max(c_B**2))
plt.ylim(0,max(vB))
plt.grid(ls='--') 
plt.legend(loc=9)

plt.tight_layout()
plt.show()


