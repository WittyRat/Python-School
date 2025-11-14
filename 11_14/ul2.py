'''Ülesanne 2 Ruutjuur 
Koosta ise funktsioon ruutjuure leidmiseks. Selleks saab kasutada Newtoni meetodit (mitte Pythoni enda sisefunktsiooni sqrt()). Meetodi tutvustus oli 4. nädala ülesandes ja vastav lahendus on 4. praktikumi lahenduste all, kuid seal ei ole kasutuses funktsiooni. Mõtle meetod läbi ja moodusta funktsioon.

Peaprogrammis kirjuta tsükkel, mis loob arvud 1..20 (näiteks for-tsüklit kasutades) ja trükib ekraanile kolme veeruga tabeli:'''
import math


def square_root(num):
    answer = num ** 0.5
    return answer

for num in range(1, 21):
    print(f"{num} \t {square_root(num)} \t {math.sqrt(num)}")