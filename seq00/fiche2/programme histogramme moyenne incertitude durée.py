import numpy as np
import matplotlib.pyplot as plt
Durée =[2.46,2.51,2.48,2.51,2.47,2.52,2.49,2.50,2.48,2.51,2.53]
plt.figure(figsize=(12,10))
plt.hist(Durée,bins=10,range=(2.45,2.55),align="mid",rwidth=0.9,color="g",edgecolor="black",label="durée")
plt.title("Durée de chute d'un objet laché d'une hauteur constante")
plt.xlabel("Durée de chute (s)")
plt.ylabel("Fréquence")
plt.legend()
plt.show()

Dt=np.mean(Durée)
ecarttype=np.std(Durée)
effectif=len(Durée)
incertitudetype=ecarttype/np.sqrt(effectif)
print("{0:2.55}".format("La durée moyenne :"),Dt,"s")
print("{0:2.55}".format("L'écart-type vaut :"),ecarttype,"s")
print("{0:2.55}".format("Le nombre de mesures vaut :"),effectif)
print("{0:2.55}".format("L'incertitude-type de répétabilité de deltat vaut :"),incertitudetype,"s")