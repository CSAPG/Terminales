import numpy as np
import matplotlib.pyplot as plt
Veprouvette =[49.61,49.55,50.91,50.87,48.03,50.29,48.58,48.06,50.06,50.72,48.95,49.4,49.21,49.31,49.78,48.77]
plt.figure(figsize=(12,10))
plt.hist(Veprouvette,bins=20,range=(45,55),align="mid",rwidth=0.9,color="b",edgecolor="red",label="éprouvette")
plt.title("Volume d'eau contenu par une éprouvette graduée pour 50mL mesuré")
plt.xlabel("Volume (mL)")
plt.ylabel("Fréquence")
plt.legend()
plt.show()


Vmoy=np.mean(Veprouvette)
ecarttype=np.std(Veprouvette)
effectif=len(Veprouvette)
incertitudetype=ecarttype/np.sqrt(effectif)
print("{0:55}".format("Le volume moyen :"),Vmoy,"mL")
print("{0:55}".format("L'écart-type vaut :"),ecarttype,"mL")
print("{0:55}".format("Le nombre de mesures vaut :"),effectif)
print("{0:55}".format("L'incertitude-type de répétabilité de deltat vaut :"),incertitudetype,"mL")