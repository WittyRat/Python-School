#Andmeteks on algselt hoiusele kantud summa, hoiustamisaastate arv ja intressimäär aasta kohta. Arvuta ja trüki välja konto seis iga hoiustamisaasta lõpus. Seda on mugavam teha for-tsükliga. Tulemus esita neljast veerust koosneva tabelina: aasta, seis aasta alguses, intress, seis aasta lõpus

def Summa():
    algne_summa = float(input("Sisesta algne summa: "))
    hoiu_aastad = int(input("Sisesta hoiustamisaastate arv: "))
    intress = float(input("Sisesta intressimäär aasta kohta (protsendides): "))
    for aasta in range(1, hoiu_aastad + 1):
        intress_summa = algne_summa * (intress/100)
        totaalne_summa = algne_summa + intress_summa
        print(f"{aasta}.aastal on seis aasta alguses {algne_summa:.2f} seis aasta lõpus {totaalne_summa:.2f}")
        algne_summa = algne_summa + intress_summa
Summa()


#Leia summa arvudele mingist etteantud vahemikust. Kasutaja sisestab vahemiku alguse ja lõpu. Programm annab vastuseks soovitud vahemikku jäävate arvude summa.

def Arvutus():
    algus = int(input("Sisesta vahemiku algus: "))
    lopp = int(input("Sisesta vahemiku lõpp: "))
    summa = 0
    
    for arv in range(algus, lopp + 1):
        summa = summa + arv
        print("Arvude summa on: ", summa)
#Arvutus()


#Koosta väike drilliprogramm korrutustabeli omandamiseks. Programm peab käituma järgmiselt (programmi põhiosa): 
#Esitab korrutustehte
#Ootab kasutajalt vastuse sisestamist 
#Kontrollib vastuse õigsust 
#Väljastab, kas vastus oli õige või väär. 
#Kokku antakse lahendamiseks 10 ülesannet. 

def Drill():
    oige_vastus = 0
    vale_vastus = 0
    for i in range(10):
        import random
        arv_1 = random.randint(1, 10)
        arv_2 = random.randint(1, 10)
        vastus = int(input(f"Mis on {arv_1} x {arv_2}? "))
        if vastus == arv_1 * arv_2:
            oige_vastus = oige_vastus + 1
            print("Õige vastus!")
        else:
            print(f"Vale vastus! Õige vastus on {arv_1 * arv_2}")
            vale_vastus = vale_vastus + 1
    print(f"Sinu tulemuseks on {oige_vastus} õiget vastust ja {vale_vastus} valesti.")

#Drill()