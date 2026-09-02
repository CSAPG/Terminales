from microbit import* # import bibliothèque micro:bit
N=int(input("Entrer le nombre de mesures voulu: "))
duree=int(input("Entrer la duree de l'acquisition en ms: "))

pin1.write_digital(0) # décharge condensateur C broche 1
sleep(5000)           # temps décharge totale en ms
pin1.write_digital(1) # charge de C sous E et R broche 1
print('t(ms)\t x')    # formatage texte affichage des résultats
t0=running_time()     # date de début de la charge
for i in range (N):        # boucle pour N mesures
    x=pin2.read_analog()   # mesure de x broche2
    date=running_time()-t0 # mesure de la date courante
    print(date,"\t",x)     # écriture des données moniteur REPL
    sleep((duree/N)-1.5)   # temporisation entre deux mesures