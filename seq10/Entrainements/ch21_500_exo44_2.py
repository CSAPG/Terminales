import serial # importation de la bibliothèque serial. 
import time   # importation de la bibliothèque time.
import numpy as np # importation de la bibliothèque numpy.
import matplotlib.pyplot as plt # importation de la bibliothèque Matplotlib 
# définition d'un objet serial_port pour gestion port série. 
serial_port=serial.Serial(port='COM22',baudrate=115200) 

serial_port.setDTR(False) # réinitialisation port serie.   
time.sleep(0.1)           # pause de 0,1 s.    
serial_port.setDTR(True)  # établissement de la connexion. 
serial_port.flushInput()  # vidage des données du buffer.
C=[]       # définition du tableau des valeurs de la capacité.
for i in range (1000):    # réception données ligne par ligne.
    l=serial_port.readline() # lecture de la ligne.
    valeur=float(chr(l[0])+chr(l[1])+chr(l[2])+chr(l[3])) # reconstitution de la valeur transférée 
    if i%100==0: print(i,'mesures') # message attente...   
    C.append(round(valeur/100,2)) # ajoute la valeur de C au tableau.       
serial_port.close()       # fermeture du port série. 
# traitement statistique des mesures
Cmoy=np.mean(C)       # calcul de la valeur moyenne de C.
u=np.std(C,ddof=1)    # calcul de l'incertitude-type u(C).
print('C =',round(Cmoy,2),'nF') # affichage C puis u(C).
print('Incertitude-type u(C) =',round(u,2),'nF') 
plt.hist(C,bins=int((max(C)-min(C))*100),color='red',edgecolor='black')
plt.title('Pour 1000 itérations')     # affichage de 
plt.xlabel('Valeur capacité C en nF') # l'histogramme en rouge  
plt.ylabel('Nombre de mesures')       # et noir.
plt.show()



