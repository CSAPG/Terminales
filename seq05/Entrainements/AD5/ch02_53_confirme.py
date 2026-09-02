#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# C02 Activité 5 page 53                                      CONFIRME
# ====================================================================
"""
Programme permettant de représenter l'évolution des quantités de  
matière des espèces en fonction du volume de solution titrante versé
La seconde partie du programme permet de tracer la conductivité de   
la solution en fonction du volume de solution titrante versé
"""

"""
Réaction support de titrage A+B->C 
A : réactif titré   cA = ? , vA
B : réactif titrant cB , vEqv
En présence d'ions spectateurs :
SA: apportés par le réactif titré
SB: apportés par le réactif titrant
"""

# importe le module pyplot de matplotlib en le renommant plt
from matplotlib import pyplot as plt

# importe NumPy en la renommant np
import numpy as np

# Saisie des informations utiles concernant la réaction étudiée
print("\nLa réaction support de titrage est :  A + B -> C")

# Existence et stoéchiométrie des ions spectateurs
test=int(input("\nY a-t-il des ions spectateurs ? " \
               "Répondre par 1 (Oui) ou 0 (Non) : "))
if test :
    print("\nPour déterminer le nombre d'ions spectateurs apportés:" \
    "\n\n-Dans (Na+,HO-), si HO- est un réactif de la réaction de" \
    " titrage :\n Na+ est un ion spectateur et il y a 1 ion Na+" \
    " apporté pour 1 ion HO-." \
    "\n\n-Dans (Fe2+,2HO-), si HO- est un réactif de la réaction de" \
    " titrage :\n Fe2+ est un ion spectateur et il y a 1/2 ion Fe2+" \
    " apporté pour 1 ion HO-.")
    coef_SA = int(input("Nombre d'ions spectateurs SA présents pour" \
                        " 1 ion titré présent : "))
    coef_SB = int(input("Nombre d'ions spectateurs SB apportés pour" \
                        " 1 ion titrant apporté : "))
else:
    coef_SA = 0
    coef_SB = 0

# Saisie des paramètres
vA=float(input("Volume initial du réactif titré en mL : vA = "))
cB=float(input("Concentration du réactif titrant en mol/L : cB = "))
vEqv=float(input("Volume de titrant versé à l'équivalence en mL : vEqv = "))

# Calcul de la concentration cA en réactif titré à partir de la 
# relation à l'équivalence : cAvA/1 = cBvEqv/1
cA=... A compléter ...

# Affichage de la concentration en réactif titré en écriture 
# scientifique avec le nombre adapté de chiffres significatifs
... A compléter ...

# Fonction calculant la composition du
# système avant l'équivalence : v<vEqv
def Avant_Eqv(v):
    nA_v = ... A compléter ...
    nB_v = 0
    nC_v = (cB*v)
    nSA_v = coef_SA*cA*vA
    nSB_v = coef_SB*cB*v
    return nA_v,nB_v,nC_v,nSA_v,nSB_v

# Fonction calculant la composition du
# système après l'équivalence (incluse) : v>=vEqv
def Apres_Eqv(v):
    nA_v = ... A compléter ...
    nB_v = ... A compléter ...
    nC_v = ... A compléter ...
    nSA_v = ... A compléter ...
    nSB_v = ... A compléter ...
    return ... A compléter ...

# Défintion du domaine des abscisses v volume versé de O à 2*vEqv avec 
# 21 valeurs régulièrement espacées (v en mL)
v = ... A compléter ... 

# Initialisation des listes vides nA,nB,nC,nSA,nSB pour 
# les quantités de matière (en mmol)
... A compléter ... 

# pour chaque valeur x du volume v de solution titrante versé
for x in v:    
# Calcul des quantités de matière notées nA_x,nB_x,nC_x,nSA_x,
# nSB_x et insertion à la fin des différentes listes pour les 
# domaines avant et après l'équivalence





   

... A compléter ... 
      








# Titre et initialisation de la fenêtre graphique
plt.figure('Quantité de matière',figsize=(7,8))

# Tracé des courbes des quantités de matière en fonction de v
# nA = ntitré = f(v)
# nB = ntitrant = f(v)
# nC = f(v)     
# S'il y a des ions spectateurs :
# Tracé en pointillé de la courbe nSA = nSpectateur-titré = f(v)
# Tracé en pointillé de la courbe nSB = nSpectateur-titrant = f(v)

... A compléter ... 


# Label des axes
# Nommer les axes des abscisses et des ordonnées
... A compléter ...    

# Limite des axes
y_max = max(max(nA),max(nB),max(nC),max(nSA),max(nSB))
plt.xlim(0,max(v)*1.1)
plt.ylim(0,y_max*1.2)

# Titre supérieur
plt.suptitle("Evolution des quantités de matière lors d'un titrage")

# Fonction affichant en titre la réaction support de titrage et les données
def titre(vA,cB,vEqv):
    reactifs = ' A$_{titré}$ + B$_{titrant}$'
    produits = ' C'
    equation = reactifs+'$ \longrightarrow $ '+produits
    data1 ='$v_{A}$ ='+str(vA)+' mL,  '
    data2 ='$c_{B}$ = '+'%.1e'%cB+' mol$\cdot$L$^{-1}$,  '
    data3 ='$v_{Eqv}$ ='+str(vEqv)+' mL'
    data=data1+data2+data3
    plt.title('Réaction support de titrage : '+equation+'\n'+data)
    return

titre(vA,cB,vEqv) # Affichage du titre (appel de la fonction titre)
plt.grid(ls='--') # Affichage d'une grille
plt.legend()      # Affichage de la légende
plt.show()


# =========== Tracé de la courbe de suivi conductimétrique ===========
"""
Supprimer les guillemets des lignes 163 et 207 pour rendre actives les
lignes de code suivantes.
"""

"""
test_2 = int(input("Voulez_vous visualiser l'allure de la courbe " \
    "de suivi conductimétrique ? Répondre par 1 (Oui) ou 0 (Non) :" ))

if test_2 : 
    print("\nConductivités molaires ioniques en mS.m^2.mol^-1 :")
    l_A=float(input("lambda_A = "))
    l_B=float(input("lambda_B = "))
    l_C=float(input("lambda_C = "))
    l_SA=float(input("lambda_SA = "))
    l_SB=float(input("lambda_SB = "))

    # Conversions des listes v, nA, nB, nC, nSA, nSB en tableaux 1D
    # nommés respectivement V, N_A, N_B, N_C, N_SA et N_SB

... A compléter ... 




    # Calcul de la conductitivité du système sigma en S.m-1 
    # pour chaque valeur de V en mL (sigma : tableau à 1D)
    # Remarque : la conductivité est obtenue en S.m-1 en combinant  
    # les concentrations en mol.L-1 et les conductivités molaires 
    # ioniques en mS.m2.mol-1
    sigma = ... A compléter ...     

    # Titre et initialisation de la fenêtre graphique
    plt.figure("Suivi conductimétrique", figsize=(7,8)) 
    
    plt.plot(V,sigma,label='$\sigma$') # Tracé de sigma = f(V)      
    
    # Mise en forme de la fenêtre graohique
    plt.suptitle("Suivi conductimétrique lors d'un titrage")
    titre(vA,cB,vEqv) # Appel de la fonction titre (cf ligne 130-140)
    plt.xlabel('Volume $v$ de solution titrante versé (en mL)')
    plt.ylabel('$\sigma$ (en S$\cdot$m$^{-1})$')
    plt.ticklabel_format(axis ='y',style='sci',scilimits=(-3,-3))
    y_max = max(sigma)
    plt.xlim(0,max(v)*1.1)
    plt.ylim(0,y_max*1.2)
    plt.grid(ls='--')
    plt.legend()    
    plt.show()
"""



