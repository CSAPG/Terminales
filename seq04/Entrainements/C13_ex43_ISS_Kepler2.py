#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 13 - Exercice 43                                    ETAPE 1     
# ====================================================================

# Partie 1 ===========================================================

"""
Cette partie permet de collecter la latitude, la longitude et l'altitude
de l'ISS depuis l'API WhereTheISS :
https://api.wheretheiss.at/v1/satellites/25544 
"""

import requests, time

date = []
latitude = []
longitude = []
altitude = []

print('\nCollecte des données de l\'ISS pour N dates espacées de ∆t secondes')
N = int(input('Nombre de dates : N = '))
delta_t = int(input('Nombre de secondes entre 2 dates : ∆t = '))

print ('\nDate (en s)\tLongitude (en °) \tLatitude (en °) \t Altitude (en km)')
for i in range(N): 
    position = requests.get('https://api.wheretheiss.at/v1/satellites/25544').json()
    date.append(position['timestamp'])
    latitude.append(float(position['latitude']))
    longitude.append(float(position['longitude']))
    altitude.append(float(position['altitude']))
    print(position['timestamp'],'\t','%.6f' %position['latitude'],'\t\t','%.6f' %position['longitude'],'\t\t','%.6f' %position['altitude'])
    time.sleep(delta_t-1) # '-1' car la durée d'acquisition à chaque requête dure environ 1 s    

# Partie 2 ===========================================================
"""
Cette partie permet de tester graphiquement la 2e loi de Kepler à
partir des données de l'ISS collectées en partie 1.
"""

b=int(input('\nVoulez-vous tester la 2e loi de Kepler à partir des données de l\'ISS ? (1=oui,0=non) = '))

if b:
    import numpy as np
    from math import cos, sin, pi
    from matplotlib import pyplot as plt
    
    R_T = 6.378137e6    # Rayon terrestre en m
    G = 6.67259e-11     # Constante de gravitation en SI

    # Translation de l'origine des dates à celle de la première série de données collectées
    t = np.array([date[i]-date[0] for i in range(N)])
    
    # Transformation des coordonnées sphériques en coordonnées cartésiennes
    r = [altitude[i]*10**3 + R_T for i in range(N)]
    x = [r[i]*cos(latitude[i]*2*pi/360)*cos(longitude[i]*2*pi/360) for i in range(N)]
    y = [r[i]*cos(latitude[i]*2*pi/360)*sin(longitude[i]*2*pi/360) for i in range(N)]
    z = [r[i]*sin(latitude[i]*2*pi/360) for i in range(N)]
    
    # Liste des aires A[i] totales balayées à la date t[i] depuis l'origine des dates
    # sachant que l'aire a d'un triangle OAB vaut a = (1/2) * norme(OA^OB)
    Aire=[0]
    aire_balayee=0
    for i in range(N-1):
        V1=np.array([x[i],y[i],z[i]])       # création du vecteur OM(i)
        V2=np.array([x[i+1],y[i+1],z[i+1]]) # création du vecteur OM(i+1)
        A=np.cross(V1,V2)           # produit vectoriel A = OM(i)^OM(i+1)
        a=(1/2)*np.linalg.norm(A)   # calcul de l'aire du triangle OM(i)M(i+1)
        aire_balayee +=a            # calcul de l'aire totale balayée depuis t0
        Aire.append(aire_balayee)   # insère l'aire totale balayée en fin de liste
    
    plt.plot(t,Aire,'+',ms=10,label='Données',clip_on=False) # Aire = f(t)
       
    m,p=np.polyfit(t,Aire,1)        # Modélisation par une droite d'équation y=m*x+p
    
    # Représentation graphique de la droite de modélisation
    X=np.linspace(0,max(t)+1,len(t))
    plt.plot(X,m*X+p,':',label='Modélisation')
    
    # Mise en forme de la fenêtre graphique
    plt.xlim(0,max(t)+1)
    plt.ylim(0,max(Aire)*1.1)
    plt.title('Test de la 2e loi de Kepler sur l\'ISS')
    plt.xlabel('Temps depuis la date $t_{0}$ de première acquisition (en s)')
    plt.ylabel('Aire balayée par le segment [TS] depuis $t_{0}$ (en m$^{2}$)')
    plt.grid(ls=':')
    plt.legend()
    plt.show()
