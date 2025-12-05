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

def summad_tabelis():
    with open("schoolClass\\t1\\tabelsis.e") as fs: #.z(4x3) ja .b(3x3)
        table = (fs.read())
        table = np.array((table.split()))

        rows = table[0]
        columns = table[1]

        #print(rows, columns)
        table = np.delete(table, [0,1])
        #print(table)
        array_size = np.size(table)
        if array_size < 6:
            print("Tabeli suurus on liiga väike, minimaalne tabel on 2x3!")
            exit() #muuta hiljem
        table = table.reshape(int(rows), int(columns))
        print(table)


        #x = np.array([])

        
        for i in range(int(rows)):
            for j in range(int(columns)-2):
                if int(table[i][j]) + int(table[i][j+1]) == int(table[i][j+2]):
                    print(f"{i+1} {j+1} R")
        
        for i in range(int(columns)):
            for j in range(int(rows)-2):
                if int(table[j][i]) + int(table[j+1][i]) == int(table[j+2][i]):
                    print(f"{j+1} {i+1} V")

        """
        offset_counter = 0

        while len(np.diagonal(table, offset=offset_counter)) > 2:
            #array_amount = len(diagonal)
            diagonal = np.diagonal(table, offset=offset_counter)
            #print(diagonal)
            for i in range(len(diagonal) -2):
                #print(diagonal[i])
                if int(diagonal[i]) + int(diagonal[i+1]) == int(diagonal[i+2]):
                    print(diagonal[i], diagonal[i+1], diagonal[i+2])
            offset_counter += 1
            """
        for offset in range(-(int(rows) - 3), int(columns) - 2):  # diagonaalid, mille pikkus on >= 3
            start_row = max(0, -offset)  # diagonaali algusrea indeks
            start_col = max(0, offset)   # diagonaali algusveeru indeks
            diag = np.diagonal(table.astype(int), offset=offset)  # võta diagonaal antud nihkega

            for i in range(len(diag) - 2):  # liigu diagonaalil kolmeste akendega
                if diag[i] + diag[i+1] == diag[i+2]:  # kontrolli A+B=C
                    row = start_row + i      # algusrea 0-põhine indeks
                    column = start_col + i   # algusveeru 0-põhine indeks
                    print(f"{row+1} {column+1} D")  # väljasta 1-põhised indeksid ja tähis D
            
board = [[f"{r}{c}" for c in range(9)] for r in range(9)]
board = np.array(board)
print(board)

