#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 13 - Exercice 43                             ETAPE 2 (PROF)     
# ====================================================================

# Partie 1 ===========================================================

"""
Cette partie permet de collecter l'altitude et la vitesse de l'ISS
depuis l'API WhereTheISS :
https://api.wheretheiss.at/v1/satellites/25544 
"""

import requests, time

altitude = [] # altitude de l'ISS en m
vitesse = []  # vitesse de l'ISS en m/s

print('\nCollecte des données de l\'ISS pour N dates espacées de ∆t secondes')
N = int(input('Nombre de dates : N = '))
t = int(input('Nombre de secondes entre 2 dates : ∆t = '))

print('\n\tAltitude (en m)\t\t Vitesse (en m/s)')

for i in range(N):
    position = requests.get('https://api.wheretheiss.at/v1/satellites/25544').json()
    altitude.append((float(position['altitude'])*1e3))
    vitesse.append((float(position['velocity'])*1e3/3600))
    print ('\t ','%.6f' %altitude[i],'\t ','%.6f' % vitesse[i])
    time.sleep(t-1) # '-1' car la durée d'acquisition à chaque requête dure environ 1 s 

# Partie 2 ===========================================================

"""
Cette partie permet d'estimer la masse de la Terre M_T en exploitant
les données collectées en partie 1 et en considérant que le mouvement
de l'ISS est modélisable par une orbite circulaire dans le champ de
gravitation newtonien de la Terre.
Soit M_T = v^2 * (R_T + h) / G
"""

b=int(input('\nVoulez-vous estimer la masse de la Terre à partir des données de l\'ISS ? (1=oui,0=non) = '))

if b:
    import numpy as np
    
    # Estimation de la vitesse de l'ISS à partir des données
    v_moy=np.mean(np.array(vitesse))             
    u_v=np.std(np.array(vitesse),ddof=1)/N**0.5
    
    # Estimation de l'altitude de l'ISS à partir des données
    h_moy=np.mean(np.array(altitude))             
    u_h=np.std(np.array(altitude),ddof=1)/N**0.5
    
    # Simulation d'une distribution d pour la valeur de la masse de la Terre
    
    # Définition d'une liste  L = [valeur,incertitude-type]
    # en unité SI pour chaque grandeur à considérer
    v=[v_moy,u_v]           # vitesse Iss (en m/s)
    h=[h_moy,u_h]           # altitude Iss (en m)
    R_T=[6.371e6,0.005e6]   # rayon de la Terre (en m)
    G=[6.673e-11,0.001e-11] # constante de gravitation (en SI)
    
    def Alea(L): # Tirage aléatoire selon la loi normale
        return np.random.normal(L[0],L[1])
    
    d=[] # Simulation d'une distribution pour M_T
    Iteration=100000
    for i in range(Iteration) :
        Alea_M_T=(Alea(v))**2*(Alea(R_T)+Alea(h))/Alea(G)
        d.append(Alea_M_T)
        
    # Valeur de M_T et de son incertitude_type u(M_T)
    M_T=np.mean(d)         # M_T <- valeur moyenne de la distribution d 
    u_M_T=np.std(d,ddof=1) # u(M_T) <- écart-type de la distribution d
        
    print('Masse de la Terre M_Terre = ','%.6e'%M_T,'kg')
    print('Incertitude-type u(M_Terre) =','%.0e'%u_M_T,'kg')