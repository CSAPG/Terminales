#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 2 Exercice 44 Exercice BAC                      CORRECTION
# ====================================================================
import numpy as np
from matplotlib import pyplot as plt

# Listes [Grandeur,incertitude-type]
m_B=[8.00,0.01]        # (en g)
V_B=[1.0,0.5e-3]       # (en L)
M_A=[176,0.5e-3]       # (en g/mol)
M_B=[40.0,0.5e-3]      # (en g/mol)
V_Eqv=[14.0e-3,0.2e-3] # (en mL)

# Tirage aléatoire selon la loi normale
def Alea(L):
    return np.random.normal(L[0],L[1])

# Simulation d'une distribution d pour m_A (en mg)
d=[]
Iteration=100000
for j in range(Iteration):
    Alea_mA=1000*Alea(m_B)*Alea(V_Eqv)*Alea(M_A)/(Alea(M_B)*Alea(V_B))
    d.append(Alea_mA)

m_A=np.mean(d)        # Valeur moyenne de d -> m_A
u_mA=np.std(d,ddof=1) # Incertitude-type de m_A

# Affichage de la masse d'acide ascorbique dans le comprimé mA et 
# de l'incertitude-type u_mA avec le nombre adapté de chiffres 
# significatifs
print('Masse d\'acide ascorbique dans le comprimé : mA = ',
'%.2f'%m_A,' mg')
print('Incertitude-type : u(mA) =','%.1f'%u_mA,' mg')

# Histogramme
plt.hist(d,bins=50,color='blue',edgecolor ='black') 
plt.xlabel('Masse d\'acide ascorbique (en mg)')
plt.ylabel('Effectif')
plt.title('Pour %i' %Iteration +' iterations')

plt.show()

