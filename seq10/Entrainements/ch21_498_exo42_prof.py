from microbit import* #import bibliothèque micro:bit
#Définition des variables
x=0   #variable tension numérisée proportionnelle à uc(t)
tau=0 #inititialisation du temps caractéristique à 0

pin0.write_digital(0) #décharge condensateur C broche0
sleep(8000)           #temps décharge totale en ms
print('Charge condensateur E=3,30 V R=100 kOhms')
pin0.write_digital(1) #charge de C sous E et R broche0
t0=running_time()     #date de début de la charge
while x<1016:         #condition d'arrêt des mesures
    x=pin2.read_analog()   #mesure de x broche2
    date=running_time()-t0 #mesure de la date courante
    if x<647:
        t1=date         # stockage de la date courante
    elif tau==0:
        tau=(date+t1)/2 # approx. lin. autour de 0,63*E
    uc=round(x*3.3/1023,2)
    print('x =',x,' \t date =',date,'ms\t    uc=',uc,'V')
print('Resultats: tau =',round(int(tau)),'ms',end='')
print(', C =',round(tau/100,2),'microFarads')
