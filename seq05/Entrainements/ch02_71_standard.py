#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 2 Exercice 44 Exercice BAC                        STANDARD
# ====================================================================
import numpy as np
from matplotlib import pyplot as plt

# Listes [Grandeur,incertitude-type]
m_B=[... A compléter...]      # (en ... A compléter...)
V_B=[... A compléter...]      # (en ... A compléter...)
M_A=[... A compléter...]      # (en ... A compléter...)
M_B=[... A compléter...]      # (en ... A compléter...)
V_Eqv=[... A compléter...]    # (en ... A compléter...)

# Tirage aléatoire selon la loi normale
def Alea(L):
    return np.random.normal(L[0],L[1])

# Simulation d'une distribution d pour m_A (en mg)
d=[]
Iteration=100000
for j in range(Iteration):
    Alea_mA=1000*Alea(m_B)*Alea(V_Eqv)*Alea(M_A)/(Alea(M_B)*Alea(V_B))
    d.append(Alea_mA)

m_A=... A compléter...    # Valeur moyenne de d -> m_A
u_mA=... A compléter...   # Incertitude-type de m_A

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





