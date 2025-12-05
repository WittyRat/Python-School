"""Ülesanne 1 Summad tabelis 
Antud on täisarvudest koosnev ristkülikukujuline tabel. Kirjutada programm, mis leiab sellest kõik kohad, kus kolm reas,
veerus või peadiagonaaliga paralleelsel diagonaalil kõrvuti olevat elementi moodustavad summa kujul A+B=C. 

Summade otsimisel vaadelda ainult kolmikuid ridades vasakult paremale, veergudes ülalt alla ja diagonaalides
vasakult-ülalt paremale-alla ning summa peab olema kolmiku viimane element.

Sisend. Tekstifaili TABEL.SIS esimesel real on tabeli ridade arv N (1 <= N <= 100) ja veergude arv M (1 <= M <= 100).
Faili järgmisel N real on igaühel M täisarvu, mille absoluutväärtus ei ületa 1000 -- tabeli elemendid ridade kaupa. 

Väljund. Tekstifaili TABEL.VAL väljastada üks rida iga leitud kolmiku kohta: kõigepealt selle esimese elemendi reanumber,
seejärel veerunumber ja seejärel täht R (kui kolmik on reas), V (kui kolmik on veerus) või D (kui kolmik on diagonaalis).
Rea- ja veerunumbri, samuti veerunumbri ja suunatähe vahele jätta tühik. Tabeli read on nummerdatud ülalt alla,
veerud vasakult paremale ning mõlemad numeratsioonid algavad 1st. Kui tabelis pole ühtki nõutud kujuga summat, 
väljastada faili esimesele reale POLE."""

import numpy as np

with open("schoolClass\\t1\\tabelsis.z") as fs: #.z(4x3) ja .b(3x3)
    table = (fs.read())
    table = np.array((table.split()))

    columns = table[0]
    rows = table[1]

    #print(rows, columns)
    table = np.delete(table, [0,1])
    #print(table)
    array_size = np.size(table)
    if array_size < 6:
        print("Tabeli suurus on liiga väike, minimaalne tabel on 2x3!")
        exit() #muuta hiljem
    table = table.reshape(int(columns), int(rows))
    print(table)

    
    for i in range(int(columns)):
        #print(table[i])
        for j in range(int(rows)-2):
            if int(table[i][j]) + int(table[i][j+1]) == int(table[i][j+2]):
                pass
                #print(i, j, table[i][j], table[i][j+1], table[i][j+2])
                print(f"{i+1} {j+1} R")
    
    for i in range(int(rows)):
        for j in range(int(columns)-2):
            #print(table[j][i], table[j+1][i], table[j+2][i])
            if int(table[j][i]) + int(table[j+1][i]) == int(table[j+2][i]):
                print(f"{j+1} {i+1} V")
            

    

