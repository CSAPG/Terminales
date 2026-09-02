#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# ====================================================================

# Chapitre 18 Exercice 40                                     STANDARD

# ====================================================================

from matplotlib import pyplot as plt
from math import pi
import numpy as np
from matplotlib.patches import Circle

T= 2.2  # Période en femtoseconde ou fs (1 fs = 1e-15 s)
t= np.linspace(......)  # 400 dates régulièrement espacées sur 4 périodes
A1=1 # Amplitude de la source 1 assimilée à un réel (unité arbitraire)
A2=1 # Amplitude de la source 2 assimilée à un réel (unité arbitraire)

# Définition, à l'aide des fonctions de la bibliothèque NumPy, de la
# fonction 's', retournant s(t)=A*cos(2πt/T+phi) pour A et phi donnés
def s(A,phi):
    return .......................

# Définition de la fonction 'interference' retournant des courbes
# modifiables grâce à la présence de la virgule (ex: 's1,').
def interference(A1,A2,phi):
    s1,= plt.plot(t,s(...,...),'--',lw=1.2,label='$s_{1}(t)$') # Trace le signal s1(t) = A1*cos(2πt/T)
    s2,= plt.plot(t,s(...,...),'--',lw=1.2,label='$s_{2}(t)$') # Trace le signal s2(t) = A2*cos(2πt/T+phi)
    S,= plt.plot(......)  # Trace le signal somme S(t) = s1(t)+s2(t)
    z,= plt.plot(......)  # Trace le carré de la somme (s1(t)+s2(t))^2
    I_phi=np.mean((s(A1,0)+s(A2,phi))**2)#Calcule l'intensité lumineuse
    I,=plt.plot(t,[I_phi]*400,'r',lw=3)#Trace l'intensité lumineuse I(t)
    plt.legend(loc=9, ncol=4)
    return s1,s2,S,z,I,I_phi



# ====================================================================
# Définitions
# - d'un cercle coloré dont la couleur est liée à l'intensité lumineuse
# - d'une barre de curseur (Slider) commandant le déphasage
# ====================================================================

from matplotlib.widgets import Slider

# Initialisation de la figure et paramétrage du repère
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.2, right=0.88, top=0.9 )

plt.title('Interférences lumineuses')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['bottom'].set_bounds(0,4.2*T)
plt.plot(4.2*T,0,marker=9, color='k', clip_on=False)
ax.text(4.25*T,0,'$temps$',va='center')
ax.set_xticks(np.linspace(0,4*T,5))
ax.set_xticklabels(['0','T','2T','3T','4T'])
ax.set_xticks((0.5*T,1.5*T,2.5*T,3.5*T), minor=True)
plt.xlim(0,4*T)
plt.ylim(-1.5*(A1+A2),1.5*(A1+A2)**2)
plt.grid(which='both',ls='--')

# Initialisation des courbes à tracer avec la valeur initiale phi =0
courbes=interference(A1,A2,0)
legende=ax.annotate(r'$I(\varphi)$',
                    (4*T,courbes[5]),(4*T+0.1, courbes[5]),
                    color='r', fontsize=14,clip_on=False)
ax.add_artist(legende)

# Initialisation du cercle coloré
rect = plt.axes([0.8, 0.07, 0.1, 0.1])
rect.spines['right'].set_color('none')
rect.spines['top'].set_color('none')
rect.spines['left'].set_color('none')
rect.spines['bottom'].set_color('none')
rect.set_xticks([])
rect.set_yticks([])

I_max=np.mean((s(A1,0)+s(A2,0))**2)
cercle=Circle((0.5,0.5),0.4,facecolor='red',alpha=courbes[5]/I_max)
cercleExt=Circle((0.5,0.5),0.4,edgecolor='grey',lw=2,alpha=0.3,fill=False)
rect.add_patch(cercle)
rect.add_patch(cercleExt)

# Définition et habillage de la barre de curseur
barre = plt.axes([0.2, 0.1, 0.5, 0.03])
curseur = Slider(barre,r'$\varphi $',-2*pi,2*pi,valinit=0,color='orange',alpha=0.7)
barre.set_xticks(np.linspace(-2*pi,2*pi,5))
barre.set_xticklabels([r'$-2\pi$',r'$-\pi$','0',r'$\pi$',r'$2\pi$'])
barre.xaxis.set_visible(True)


# Mise à jour de la figure selon la position du curseur
def update(val):
    # phi est la valeur du déphasage liée à la position du curseur
    phi = curseur.val
    I_phi=np.mean((s(A1,0)+s(A2,phi))**2)
    # Mise à jour des courbes à tracer et du cercle à colorer
    courbes[1].set_ydata(s(A2,phi))
    courbes[2].set_ydata(s(A1,0)+s(A2,phi))
    courbes[3].set_ydata((s(A1,0)+s(A2,phi))**2)
    courbes[4].set_ydata([I_phi]*400)
    cercle.set_alpha(I_phi/I_max)
    legende.set_y(I_phi)
    # Mise à jour de la figure
    fig.canvas.draw_idle()

# Mise à jour à chaque nouvelle position du curseur
curseur.on_changed(update)

plt.show()
