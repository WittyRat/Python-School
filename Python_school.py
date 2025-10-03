hinne_a = 0
hinne_b = 0
hinne_c = 0
hinne_d = 0
hinne_e = 0
hinne_f = 0

key = "j"

max_points = int(input("Siesta maksimum punktide arv: "))

while key == "j":
    points = int(input("Sisesta kontrolltöö punktid: "))
    procent_points = points / max_points * 100
    print(procent_points)

    if procent_points > 100:
        print("Viga! Punktide arv on liiga suur!")
    elif procent_points >= 90:
        hinne_a = hinne_a + 1
    elif procent_points >= 80:
        hinne_b = hinne_b + 1
    elif procent_points >= 70:
        hinne_c = hinne_c + 1
    elif procent_points >= 60:
        hinne_d = hinne_d + 1
    elif procent_points >= 50:
        hinne_e = hinne_e + 1
    else:
        hinne_f = hinne_f + 1


    key = input("Kas soovid veel punkte sisestada? (j/e): ")

print("hindeid A on kokku: ", hinne_a, "\nhindeid B on kokku: ", hinne_b, "\nhindeid C on kokku: ", hinne_c, "\nhindeid D on kokku: ", hinne_d, "\nhindeid E on kokku: ", hinne_e, "\nhindeid F on kokku: ", hinne_f)