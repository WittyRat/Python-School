#Tanel_Metshein_1.py
#jaak = 241220 % 7
#print(jaak)

# Kui kaua kulus ligikaudu aega ülesande lahendamiseks?
    #ligikaudu 5 kuni 10 minutit

# Kas ja millised süntaksivead peamiselt tekkisid?
    #ei tekkinud ühtegi viga

# Kas tekkis erineid ehk täitmisaegseid vigu?
    #ei tekkinud ühtegi viga

# Kas programmis oli ka loogikavigu? Kuidas need avastasid ja parandasid?
    #ei tekkinud ühtegi viga



#Programmi ülesandeks on tuvastada paarisarvud ja leida nende summa. Programm küsib kasutajalt, mitu täisarvu ta sisestada soovib. Seejärel laseb sisestada arve, leiab summat ja trükib iga paarisarvu korral ekraanile sobiliku teate. Paarisarvude summa trükitakse lõpuks üks kord vastusena välja. Paaritute arvude peale ei regeeri programm mitte mingil viisil.

kordus = int(input("Mitu täisarvu soovid sisestada? "))
taisarv_summa = 0

for arv in range(kordus):
    taisarv = int(input("Sisesta täisarv: "))
    if taisarv % 2 == 0:
        print(f"{taisarv} on paaris arv")
        taisarv_summa = taisarv_summa + taisarv
    else:
        pass
print("Paarisarvude summa on: ", taisarv_summa)