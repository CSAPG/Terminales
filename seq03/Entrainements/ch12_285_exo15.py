#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Chapitre 12 Exercice 15                                            Correction 
# =============================================================================
import matplotlib.pyplot as plt
m = 75   # Masse en kg
g = 9.81 # Intensité de la pesanteur en N/kg
# =============================================================================
# Etape 1 : Importation des données de pointage
# =============================================================================
t,z=[],[]  # Définitions de listes vides pour t et z
with open('C12_Exercice15_saut_elastique.txt') as fichier:
    header = [fichier.readline() for i in range(1)]
    line = fichier.readline().replace(',','.')
    while line:
        data0,data1=line.split('\t') 
        t.append(float(data0)) 
        z.append(float(data1)) 
        line=fichier.readline().replace(',','.')
# =============================================================================
#  Etape 2 : Calcul de la coordonnée vz et de la norme v du vecteur vitesse 
# =============================================================================
N = len(t) # Nombre de positions
vz,v = [],[] # Définitions de listes vides pour vz et v
for i in range(N-1) : 
    vzi=(z[i+1]-z[i])/(t[i+1]-t[i]) 
    vi=abs(vzi)    
    vz.append(vzi) 
    v.append(vi)   
# =============================================================================
# Etape 3 : Calcul des grandeurs énergétiques
# =============================================================================
Epp,Ec,Em = [],[],[] # Définitions de listes vides pour Epp, Ec et Em
for i in range(N-1) : 
    Eppi=m*g*z[i]        # calcul de l'énergie potentielle de pesanteur
    Eci=(1/2)*m*v[i]**2  # calcul de l'énergie potentielle de pesanteur
    Emi=Eci+Eppi         # calcul de l'énergie mécanique
    Epp.append(Eppi) 
    Ec.append(Eci)   
    Em.append(Emi) 
# =============================================================================
# Etape 4: Représentation graphique
# =============================================================================
del t[-1] # Suppression du dernier élément de la liste t
plt.plot(t,Epp,color='b',marker='+', label = '$E_{pp}$')
plt.plot(t,Ec,color='r',marker='x', label = '$E_{c}$')
plt.plot(t,Em,color='g',marker='o', label = '$E_{m}$')
plt.title("Evolution des différentes formes d'énergie au cours du temps", fontsize = 10)   
plt.xlabel("$t$ (en s)")              
plt.ylabel("Energie ( en $10^{3}$J)")
plt.ticklabel_format(axis='y',style='scientific',scilimits=(3,3))         
plt.legend()
plt.grid()                    
plt.show()

