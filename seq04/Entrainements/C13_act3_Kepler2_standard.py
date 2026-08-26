#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 13 Activité 3                                      STANDARD
# ====================================================================
"""
Ce programme permet de tester la deuxième loi de Kepler en exploitant
le fichier AD3-donnees1.txt qui contient l'éphéméride des positions
quotidiennes de la Terre sur une année collectées depuis le site
http://vo.imcce.fr/webservices/miriade/?forms.
Les lignes commençant par # et la ligne d'intitulé des grandeurs du
fichier directement issu du site en format .txt ont été supprimées.
"""
# ============ Extraction des données : NE PAS MODIFIER ==============

#Fonction permettant de convertir la longitude sous forme décimale
def decimale_long(d):
    deg=int(d[1:4])
    minute=int(d[5:7])/60
    seconde=(int(d[8:10])+int(d[11:15])/10000)/3600
    return float(deg+minute+seconde)

# Instructions permettant l'extraction des données
longitude=[]
distance=[]
  
with open('AD3-donnees1.txt') as fichier:
    line = fichier.readline()
    while line:
        data0,data1,data2,data3,data4,data5=line.split(',')
        longitude.append(decimale_long(data2))
        distance.append(float(data4))
        line = fichier.readline()

# ============ Extrait de code de l'énoncé ===========================

from math import pi

# Fonction calculant l'aire d'un secteur circulaire
# de rayon 'r' en mètre et d'angle au centre 'angle' en degré
def aire(angle,r):
    aire=(pi*angle*r**2)/360
    return aire

ua=1.495978707e11 # unité astronomique (en mètre)

n = int(input('Choisir le nombre n de jours (0<n<364) pour ∆t = ' ))

# Fonction calculant l'aire balayée pendant ∆t depuis une position j
def Aire_Delta_t(j,n):
    aire_balayee=0
    for i in range(n):
        angle=longitude[j+i+1]-longitude[j+i]
        r=distance[j+i]*ua
        a=aire(angle,r)
        aire_balayee = aire_balayee + a
    return aire_balayee   

# ============ Programme à compléter =================================

from matplotlib import pyplot as plt
import numpy as np

# Liste des aires balayées pendant ∆t
# depuis chaque position de l'éphéméride       
N = len(longitude)   
...A complèter... # Initialisation d'une liste vide 'Aire'
...A complèter... # pour chaque position i de l'éphéméride pour laquelle le calcul est possible
...A complèter... # Calcule l'aire balayée pendant ∆t depuis la position i
...A complèter... # Insère cette valeur en fin de liste Aire
    
# Etude statistique de la série de mesures de l'aire balayée pendant ∆t
...A complèter... # Valeur moyenne de la liste Aire
...A complèter... # Incertitude-type de la liste Aire

# Affichage de l'histogramme des aires balayées pendant ∆t
...A complèter... # Tracé de l'histogramme
...A complèter... # Titre de l'histogramme 
...A complèter... # Label de l'axe des abscisses
...A complèter... # Label de l'axe des ordonnées

# Affichage du résultat de l'étude statistique
print('\nAire A balayée pendant ∆t =',n,'jours :')
print('\nValeur moyenne de A :',...A complèter...)
print('\nIncertitude-type : u(A) =',...A complèter...)


