# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 3 Exercice 38                                      CONFIRME 
# ====================================================================
import matplotlib.pyplot as plt
import numpy as np

c_t=0.040   #conc. en quantité de la solution titrante (en mol/L)
c_1=0.20    #conc. en quantité de la solution d'ion iodure (en mol/L)
V_1=0.050   #volume de la solution d'ion iodure (en L)
V_tot=0.100 #volume total du mélange réactionnel (en L)
V_2=0.010   #volume du prélèvement (en L)

# ====================================================================
# Saisie des données expérimentales
# ====================================================================
t=[1.0,3.0,4.5,6.0,8.5,12.0,15.0,18.0,24.0]   # t (en min)
V_eq=[2.2,4.8,6.3,7.3,9,10.8,11.7,12.7,13.7]  # Véqv (en mL)
N=len(t)
# ====================================================================
# Calcul de la quantité de diiode titrée aux dates ti
# ====================================================================
n_I2=[] 
for i in range(N) : 
    n_I2i=...A compléter... # qté de matière de I2 titrée (en mol)
    n_I2.append(n_I2i) 

# ====================================================================
# Calcul de la concentration en quantité des ions iodure aux dates ti
# ====================================================================
c_I=[] 
for i in range(N) : 
    c_Ii=...A compléter... # [I-] aux dates ti (en mol/L)
    c_I.append(c_Ii) 

# ====================================================================
# Affichage des valeurs numériques: Date, n(I2) titré, [I-] en colonne
# ====================================================================
...A compléter...
...
...
...    

# ====================================================================
# Test d'une loi de vitesse d'ordre 1 pour l'évolution de [I-]
# ====================================================================

plt.figure(figsize=(16,4))
plt.suptitle("Test d'une loi d'ordre 1 pour l'évolution de [I$^{-}$]")   

"""
Méthode 1 :
L’évolution de la concentration en ion iodure suit une loi de vitesse
d’ordre 1 si ln([I-](t)/[I-](t=0)) est une fontion linéaire du temps.
"""
plt.subplot(1,2,1)

# Définition d'une liste 'date' de toutes les dates en seconde de t=0s à tmax
...A compléter...
...

# Définition d'une liste 'Y' des valeurs de ln([I-](t)/[I-](t=0)) de t=0s à tmax
...A compléter...
...

# Tracé de ln([I-](t)/[I-](t=0)) = f(t) de t=0s à tmax, nommé 'Points expérimentaux'
...A compléter...

# Modélisation de la forme y=a*x+b à l'aide de la fonction np.polyfit()
a,b=...A compléter...
modele=[...A compléter... for i in ...A compléter...] # Calcul des ordonnées du modéle

# Tracé de la modélisation : modele = f(date), nommé 'Modélisation linéaire'
...A compléter...

# Mise en forme de la fenêtre graphique
plt.text(600,-0.2,"$\ln\dfrac{[\mathrm{I}^{-}](t)}{[\mathrm{I}^{-}](t=0)}=f(t)$",fontsize=14,color='r')
...A compléter...  # Label de l'axe des abscisses            
...A compléter...  # Affichage d'une grille en ':'
...A compléter...  # Affichage de la légende en bas à gauche

"""
Méthode 2 :
L’évolution de la concentration en ion iodure suit une loi de vitesse
d’ordre 1 si la vitesse de consommation des ions iodures v_I est
proportionnelle à [I-].
"""    
plt.subplot(1,2,2)

# Liste des vitesses de consommation en ion iodure en mol/L/s
c_I.insert(...A compléter...) # insère [I-](t=0)=c_1/2 en début de liste c_I
v_I=[...A compléter... for i in ...A compléter...]

...A compléter... # Retire la dernière valeur de la liste c_I

# Tracé de v_I = f(c_I),nommé 'Points expérimentaux'
...A compléter...

# Modélisation de la forme y=a*x+b à l'aide de la fonction np.polyfit()
m,p=...A compléter...
mod=[...A compléter...] # Calcul des ordonnées du modéle

# Tracé de la modélisation mod = f(c_I), nommé 'Modélisation linéaire'
...A compléter...

# Mise en forme de la fenêtre graphique
plt.text(0.02,8e-5,"$v_{c,\mathrm{I}^-}=f(t)$",fontsize=14, color='r')
plt.ticklabel_format(axis='both',style='sci',scilimits=(0,0))
...A compléter...  # Label de l'axe des abscisses
...A compléter...  # Label de l'axe des ordonnées           
...A compléter...  # Limite de l'axe des abscisses 
...A compléter...  # Limite de l'axe des ordonnées 
...A compléter...  # Affichage d'une grille en ':'
...A compléter...  # Affichage de la légende en haut à droite
plt.show()


