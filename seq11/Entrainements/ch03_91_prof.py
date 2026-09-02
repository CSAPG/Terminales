# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 3 Exercice 38                                    Correction 
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
    n_I2i=5*c_t*V_eq[i]*1e-3 # qté de matière de I2 titrée (en mol)
    n_I2.append(n_I2i) 

# ====================================================================
# Calcul de la concentration en quantité des ions iodure aux dates ti
# ====================================================================
c_I=[] 
for i in range(N) : 
    c_Ii=c_1/2-5*c_t*V_eq[i]*1e-3/V_1 # [I-] aux dates ti (en mol/L)
    c_I.append(c_Ii) 

# ====================================================================
# Affichage des résultats
# ====================================================================
print('\nDate t \t\t n(I2) titré \t\t [I-]')
print('(en min) \t (en mol) \t\t (en mol/L)')
for i in range(N):
    print(t[i],'\t\t','%.2e'%n_I2[i],'\t\t','%.2e'%c_I[i])

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

# Liste des dates en seconde de t=0s à tmax
date=[t[i]*60 for i in range(N)]  # conversion des dates ti en s 
date.insert(0,0) # insère 0 au début de la liste 'date'

# Liste des valeurs de ln([I-](t)/[I-](t=0)) de t=0s à tmax
Y=[np.log(c_I[i]/(c_1/2)) for i in range(N)]#Calcul du ln aux dates ti
Y.insert(0,0) # insère 0 au début de la liste 'Y'

# Tracé de ln([I-](t)/[I-](t=0)) = f(t) de t=0s à tmax
plt.plot(date,Y,'b+',label='Points expérimentaux')

# Modélisation de la forme y=a*x+b à l'aide de la fonction np.polyfit()
a,b=np.polyfit(date,Y,1)
modele=[a*date[i]+b for i in range(N+1)]

# Tracé de la modélisation
plt.plot(date,modele,'c:',label='Modélisation linéaire')

# Mise en forme de la fenêtre graphique
plt.text(600,-0.2,"$\ln\dfrac{[\mathrm{I}^{-}](t)}{[\mathrm{I}^{-}](t=0)}=f(t)$",fontsize=14,color='r')
plt.xlabel("$t$ (en s)")             
plt.grid(ls=':') 
plt.legend(loc=3)

"""
Méthode 2 :
L’évolution de la concentration en ion iodure suit une loi de vitesse
d’ordre 1 si la vitesse de consommation des ions iodures v_I est
proportionnelle à [I-].
"""    
plt.subplot(1,2,2)

# Liste des vitesses de consommation en ion iodure en mol/L/s
c_I.insert(0,c_1/2) # insère [I-](t=0)=c_1/2 en début de liste c_I
v_I=[-(c_I[i+1]-c_I[i])/(date[i+1]-date[i]) for i in range(N)]

del c_I[-1] # Retire la dernière valeur de la liste c_I

# Tracé de v_I = f(c_I)
plt.plot(c_I,v_I,'b+',label='Points expérimentaux')

# Modélisation de la forme y=a*x+b à l'aide de la fonction np.polyfit()
m,p=np.polyfit(c_I,v_I,1)
mod=[m*c_I[i]+p for i in range(N)]

# Tracé de la modélisation
plt.plot(c_I,mod,'c:',label='Modélisation linéaire')

# Mise en forme de la fenêtre graphique
plt.text(0.02,8e-5,"$v_{c,\mathrm{I}^-}=f(t)$",fontsize=14, color='r')
plt.ticklabel_format(axis='both',style='sci',scilimits=(0,0))
plt.xlabel('[I$^-$] (en mol$\cdot$L$^{-1}$)')
plt.ylabel('$v_{C,I^-}$ (en mol$\cdot$L$^{-1}\cdot$s$^{-1}$)')
plt.xlim(0,max(c_I))
plt.ylim(0,max(v_I))
plt.grid(ls=':') 
plt.legend(loc=1)

plt.show()


