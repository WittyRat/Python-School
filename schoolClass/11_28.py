import numpy as np
import random

"""Ülesanne 1 Tärnid
Moodusta ekraanile tärnidest ruut. Ruudu külgede pikkuse sisestab kasutaja. Näiteks kui ruudu külg on 5"""

def tarnid():
    [print(5*"*")for _ in range(5)]





"""Ülesanne 2 Korrutustabel NB! Kasutada tsükleid ja loomulikult tuleb tabel lõpuni täita! 

Tegevuste järjekord: 

1. Moodusta sobivad tegurite paarid. Pane kaks range()-funktsiooni kasutavat for-tsüklit teineteise sisse (nagu 1. ülesandes) ja vaata, milliseid väärtuseid saavad tsüklimuutujad.

2. Korruta tegurid. 

3. Saavuta tabelilaadne kuju (formaadiga väljatrükk, kasutades välja laiust, vt näidet valjund_7.py.

4. Lisa tabelile igasugused päised. """

def mult_table():
    row = list(range(1, 11))
    column = list(range(1, 11))

    table = [[r * c for r in row] for c in column]


    [print("\t", num, end="") for num in range(1,11)]
    print(f"\n\t{20*"____"}")
    [[print(f"{i+1}\t|", end=""), [print(f"{table[i][j]:2d}", end="\t") for j in range(10)], print(end="|\n")] for i in range(10)]
    #14 row -> expanded
    #for i in range(10):
    #    print(f"{i+1}\t|", end="")
    #    for j in range(10):
    #        print(mult_table()[i][j], end="\t")
    #    print(end="|\n")



"""NB! Kasutada tsükleid ja loomulikult tuleb tabel lõpuni täita! 

Tegevuste järjekord: 

1. Moodusta sobivad tegurite paarid. Pane kaks range()-funktsiooni kasutavat for-tsüklit teineteise sisse (nagu 1. ülesandes) ja vaata, milliseid väärtuseid saavad tsüklimuutujad.

2. Korruta tegurid. 

3. Saavuta tabelilaadne kuju (formaadiga väljatrükk, kasutades välja laiust, vt näidet valjund_7.py.

4. Lisa tabelile igasugused päised. 

Edasi uurime kahemõõtmelist massiivi ehk Pythoni kontekstis listi, mille elementideks on listid."""


def magic_square(row, columns):
    if row != columns:
        print("read ja veerud ei ole sama suured")
        row = int(input("Sisesta ridade arv: "))
        columns = int(input("Sisesta veerude arv: "))
    sums = list()
    #times_cube_created = 0

    slots = row * columns
    #while True:
        #cube = np.array([[2, 7, 6],[9, 5, 1],[4, 3, 8]])
    cube = np.random.randint(1, 9, size=slots)
    cube = cube.reshape(row, columns)
    print(cube)

    diagonal_1 = np.fliplr(cube).diagonal() #fliplr on [:, ::-1]
    sum_dia_1 = sum(diagonal_1)
    sums.append(int(sum_dia_1))

    diagonal_2 = np.diagonal(cube)
    sum_dia_2 = sum(diagonal_2)
    sums.append(int(sum_dia_2))


    for i in range(row):
        sum_axis_0 = np.sum(cube, axis = 0)[i]
        sums.append(int(sum_axis_0))
            
        sum_axis_1 = np.sum(cube, axis = 1)[i]
        sums.append(int(sum_axis_1))

    if sums[:-1] == sums[1:]:
        print("Maagiline ruut")
    else:
        print("Ei tulnud maagiline ruut")
        #print(times_cube_created)
        #break
    #times_cube_created += 1 

roww = int(input("Sisesta ridade arv: "))
columnss = int(input("Sisesta veerude arv: "))
magic_square(roww, columnss)
    
    

