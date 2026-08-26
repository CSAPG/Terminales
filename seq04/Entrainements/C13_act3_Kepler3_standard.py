#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =====================================================================
# Chapitre 13 Activité 3                                       STANDARD
# =====================================================================
"""
Ce programme permet de tester la troisème loi de Kepler à partir des
données (demi grand axe et période de révolution) des planètes du
système solaire regroupées dans le fichier AD3-donnees2.txt.
"""
# ============ Extraction des données : NE PAS MODIFIER ==============
import numpy as np

with open('AD3-donnees2.txt') as fichier:
    header = [fichier.readline() for i in range(5)]
    a=np.array([float(i) for i in fichier.readline().split(';')])
    T=np.array([float(i) for i in fichier.readline().split(';')])

# ============ Programme à compléter =================================

from matplotlib import pyplot as plt

x=...A compléter...   # Grandeur à porter sur l'axe des abscisses 
y=...A compléter...   # Grandeur à porter sur l'axe des ordonnées

k,b=...A compléter... # Modélisation par une droite d'équation y=k*x+b

# Affichage du nuage de points et de sa modélisation
...A compléter...     # Tracé du nuage de points (x,y) légendé
...A compléter...     # Tracé de sa modélisation légendée
...A compléter...     # Label de l'axe des abscisses
...A compléter...     # Label de l'axe des ordonnées
...A compléter...     # Affichage de la légende
...A compléter...     # Affichage d'une grille
...A compléter...     # Affichage de la figure


