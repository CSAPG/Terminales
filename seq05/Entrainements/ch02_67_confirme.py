#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##====================================================================
# Chapitre 02 Exercice 38                                     CONFIRME
#=====================================================================

from matplotlib import pyplot as plt

n0=............ # Quantité de matière de nigari introduite (en mmol)
cB=0.20         # Concentration en (Na+,OH-) (en mol/L)
vEqv=.......... # Calcul du volume équivalent (en mL)
v=[i*vEqv/10 for i in range(21)]  # Volume versé de 0 mL à 2*vEqv
nA,nB,nC,nS_A,nS_B=[],[],[],[],[] # Listes des quantités de matière
for x in v:
    if x<vEqv:
        nA.append(n0-cB*x/2)
        nB.append(0)
        nC.append(cB*x/2)
        nS_A.append(2*n0)  # Ions spectateurs
        nS_B.append(cB*x)  # Ions spectateurs
    else:
        nA.append(0)
        nB.append(cB*x - cB*vEqv)
        nC.append(cB*vEqv/2)
        nS_A.append(2*n0)  # Ions spectateurs
        nS_B.append(cB*x)  # Ions spectateurs 

plt.figure('Quantité de matière',figsize=(7,8))
plt.plot(v,nA,label='$n_{A}=n_{titré}$')
plt.plot(v,nB,label='$n_{B}=n_{titrant}$')
plt.plot(v,nC,label='$n_{C}$')
plt.plot(v,nS_A,':',label='$n_{Spectateur-titré}$')    
plt.plot(v,nS_B,':',label='$n_{Spectateur-titrant}$')

# Label des axes
plt.xlabel('Volume $v$ de solution titrante versé (en mL)')
plt.ylabel('Quantité de matière des espèces (en mmol)')

# Limite des axes
y_max = max(max(nA),max(nB),max(nC),max(nS_A),max(nS_B))
plt.xlim(0,max(v))
plt.ylim(0,y_max*1.1)

# Titre supérieur
plt.suptitle("Evolution des quantités de matière lors d'un titrage")

# Titre affichant la réaction support de titrage et les données
reactifs = ' Mg$^{2+}$(aq) + 2 OH$^{-}$(aq)'
produits = ' MgOH$_{2}$(s)'
equation = reactifs+'$ \longrightarrow $ '+produits

data1 ='$c_{B}$ = '+'%.2f'%cB+' mol$\cdot$L$^{-1}$,  '
data2 ='$n_{A,debut}$ ='+'%.2f'%(n0)+' mmol,  '
data3 ='$v_{Eqv}$ ='+'%.1f'%vEqv+' mL'
data=data1+data2+data3
plt.title('Réaction support de titrage : '+equation+'\n'+data)

# Affichage d'une grille et de la légende
plt.grid(ls='--')
plt.legend()
plt.show()

import numpy as np

# =========== Tracé de la courbe de suivi conductimétrique ===========
"""
Supprimer les guillemets des lignes 71 et 134 pour rendre actives les
lignes de code suivantes.
"""  

"""
test_2 = int(input("Voulez_vous visualiser l'allure de la courbe " \
    "de suivi conductimétrique ? Répondre par 1 (Oui) ou 0 (Non) :" ))

if test_2 : 
    vA=float(input('\Volume initial du réactif titré en mL : vA = '))
    print("\nConductivités molaires ioniques en mS.m^2.mol^-1 :")
    l_A=float(input("lambda_A = "))
    l_B=float(input("lambda_B = "))
    l_C=float(input("lambda_C = "))
    l_S_A=float(input("lambda_S_A = "))
    l_S_B=float(input("lambda_S_B = "))

    # Conversions des listes v, nA, nB, nC, nS_A, nS_B en tableaux 1D,
    # nommés respectivement V, N_A, N_B, N_C, N_S_A, N_S_B
 

    ... A compléter ...

   

    # Calcul de la conductitivité du système sigma en S.m-1 
    # pour chaque valeur de V en mL (sigma : tableau à 1D)
    sigma = ... A compléter ... 
    

    # Titre et initialisation de la fenêtre graphique
    plt.figure('Suivi conductimétrique', figsize=(7,8))   

    # Tracé de sigma = f(V)
    ... A compléter ...       

    # Label des axes
    ... A compléter ...    
    

    # Axe des ordonnées en écriture scientifique
    plt.ticklabel_format(axis ='y',style='scientific',scilimits=(0,0)) 

    # Limite des axes
    y_max = max(sigma)
    plt.xlim(0,max(v)*1.1)
    plt.ylim(0,y_max*1.2)

    # Titre supérieur
    plt.suptitle('Suivi conductimétrique lors d\'un titrage')

    # Titre affichant la réaction support de titrage et les données
    reactifs = str(a)+ ' A$_{titrant}$ + ' +str(b)+r' B$_{titré}$'
    produits = str(c)+' C'
    equation = reactifs+'$ \longrightarrow $ '+produits

    data1 ='$c_{A}$ = '+'%.1e'%cA+' mol$\cdot$L$^{-1}$,  '
    data2 ='$n_{B,début}$ ='+str(nB_debut)+' mmol,  '
    data3 ='$v_{Eqv}$ ='+str(vEqv)+' mL'
    data=data1+data2+data3

    plt.title('Réaction support de titrage : '+equation+'\n'+data)

    # Affichage d'une grille et de la légende
    plt.grid(ls='--')
    plt.legend()
    plt.show()
"""



