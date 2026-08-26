#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =================================================================================
# Chapitre 11 : Mouvements et force
# Exercice  25  : Modéliser un mouvement rectiligne
# Programme permettant de modéliser le mouvement d'un mobile de masse m soumis à
# une unique force constante, sur une table horizontale. Le programme
# permet de représenter les positions et les vecteurs accélération d'une masse m
# soumise à une force dont on peut indiquer la valeur.
# =================================================================================
"""
Les blocs de lignes de codes entre 2 séries de 3 guillemets sont des commentaires:
ils sont inactifs lors de l'exécution du programme .
"""
"""
1.Exécuter le code source pour visualiser la figure produite. Justifier que seules
  les coordonnées sur l'axe x soient prises en compte pour les calculs de vitesse.
2.Réaliser ensuite plusieurs simulations en faisant varier la norme de la force
  exercée sur la masse m et conclure sur l'influence de la norme de la force
  sur le vecteur accélération.
"""
import numpy as np
from matplotlib import pyplot as plt

# ==== Définition des variables et constantes nécessaires =========================
dt=0.025 # Valeur de l'intervalle de temps constant et égale à 25 ms
F =float(input('Valeur F de la force (entre 0,1 et 0,5 N): F = ? '))
m=float(input('Valeur de la masse m (entre 0,100 et 0,500 kg): m = ? '))
N =20     # Nombre maximal de points à représenter

# ==== Génération des coordonnées de la masse ponctuelle m ========================
t = np.linspace(0,N*dt,N)         # Définition du domaine des dates (en s)
x = 100*((F/(2*m))*t**2)        # Définition des abscisses x (en cm)
y = 100*(0*t + 0.00)            # Définition des ordonnées y (en cm)
# distance en cm pour alléger la représentation graphique

# ==== Figures représentant les trajectoires y1=f(x1) et y2=f(x2) ==================
plt.figure('Positions et vecteurs accélération de m')
plt.title('Vecteur accélération de m'+' (F='+str(round(F,2))+' N)')
plt.xlabel('x(en cm)')
plt.ylabel('y(en cm)')
plt.plot(x,y,'bo',ms=2,label='masse m='+str(m)+' kg')
plt.axis([-0.1,1.9,-0.4,0.4])

# ==== Calculs des coordonnées des vecteurs vitesse V =======================
# définition d'une liste pour les variables Vx
Vx=[0]
for i in range(1,len(t)-1) :
    # calcul des coordonnées Vxi des vecteurs vitesse sur l'axe x au point n°i
    Vxi=(x[i+1]-x[i])/(t[i+1]-t[i])
    Vx.append(Vxi)                # ajout de la valeur Vxi à la liste Vx

# ==== Tracé des vecteurs accélération  ==================
for i in range(2,len(t)-2) :
    # Représente, au point d'indice i de coordonnées (x[i],y[i]), une flèche
    # de longueur (Vx[i+1]-Vx[i-1])/(2*dt) sur l'axe x
    plt.arrow(x[i],y[i],0.001*(Vx[i+1]-Vx[i-1])/(2*dt),0,width=0.005,
    length_includes_head="true",head_length=0.04,head_width=0.03,color='g')

       # affichage des valeurs des vecteurs accélération dans l'interpréteur
    # uniquement pour les vecteurs représentés dans la fenêtre graphique
    if(x[i]<=1.9) :
        print("a =",round(((Vx[i+1]-Vx[i-1])/(2*dt)),2),"cm.s-2")

#-affichage de l'échelle de représentation des vecteurs accélération - A NE PAS MODIFIER
plt.text(0,-0.30,'Echelle du vecteur accélération :', color='green')
plt.text(1.25,-0.35,10, color='green')
plt.text(1.32,-0.35,' cm.s$^{-2}$', color='green')
# flèche de longueur correspondant à 0,20 m/s²
plt.arrow(1.27,-0.3, dt*10, 0,width=0.005,
              length_includes_head="true", head_length=0.04,
              head_width=0.03, color='g')

plt.legend()
plt.show()