'''Ülesanne 1 Ringi pindala 
Koosta funktsioon, mis arvutab ringi raadiuse järgi ringi pindala. Funktsiooni argumendiks on ringi raadius ja funktsioon tagastab ringi pindala.

Koosta teine funktsioon, mis leiab kauguse kahe punkti vahel. Funktsiooni argumentideks on mõlema punkti x ja y koordinaadid ning funktsioon tagastab punktide-vahelise kauguse.

Lisa programm, mis küsib ringi keskpunkti ja ühe ringjoonel oleva punkti x ja y koordinaadid ning arvutab välja ringi pindala. Vastuse leidmiseks kutsutakse välja funktsioon punktide-vahelise kauguse leidmiseks (see on raadius) ja seejärel teine funktsioon pindala leidmiseks. 

NB! Kumbki funktsioon ei trüki midagi ekraanile. Kasutajaga suhtleb peaprogramm.'''




def area_circle(radius):
    from math import pi, sqrt

    area_of_circle = pi * radius**2
    return round(area_of_circle, 2)

def distance_points_1d(x, y):
    distance_1d = abs(y-x)
    return distance_1d

def distance_points_2d(x1, y1, x2, y2):
    from math import sqrt

    distance_2d = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance_2d

#arvutab ringi pindala, keskpunktiga ja punktiga mis on ringjoonel
def area_of_circle(x1, y1, x2, y2):
    from math import pi, sqrt

    distance = sqrt(((x2-x1)**2)+((y2-y1)**2))
    area = pi * distance**2
    return round(area, 2)

choice = input("1) ringi pindala arvutamine antud raadiusega\n2) kahe punkti vaheline kaugus ühe koordinaadiga\n3) kahe punkti vaheline kaugus kahe koordinaadiga\n4) arvutamine ringi pindala, keskpunkti ja punkiga, mis asub ringjoonel\n")

if choice == "1":
    circle_radius = float(input("Sisesta ringi raadius\n"))
    print(area_circle(circle_radius))

elif choice == "2":
    x_cord = float(input("Sisesta X koordinaat\n"))
    y_cord = float(input("Sisesta Y koordinaat\n"))
    print(distance_points_1d(x_cord, y_cord))

elif choice == "3":
    x_x_cord, x_y_cord = float(input("Sisesta Esimese punkti koordinaadid (x, y)\nEsimese punkti X koordinaat: ")), float(input("Esimese punkti Y koordinaat: "))
    y_x_cord, y_y_cord = float(input("Sisesta Teise punkti koordinaadid (x, y)\nTeise punkti X koordinaat: ")), float(input("Teise punkti Y koordinaat: "))
    print(distance_points_2d(x_x_cord, x_y_cord, y_x_cord, y_y_cord))

elif choice == "4":
    x_x_cord, x_y_cord = float(input("Sisesta Esimese punkti koordinaadid (x, y)\nEsimese punkti X koordinaat: ")), float(input("Esimese punkti Y koordinaat: "))
    y_x_cord, y_y_cord = float(input("Sisesta Teise punkti koordinaadid (x, y)\nTeise punkti X koordinaat: ")), float(input("Teise punkti Y koordinaat: "))
    print(area_of_circle(x_x_cord, x_y_cord, y_x_cord, y_y_cord))

else:
    print("Vale valik!")