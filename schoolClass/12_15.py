"""Ülesanne 1 Odaviske võistlus
Programmi töö aluseks on andmed odaviske võistluse tulemuste kohta. Selleks on sportlase nimi
ja kolme viske tulemused. Andmed on nö lihtsustatud, ehk parim vise tuleb leida kolme viske hulgast. 

Leida võitja. Andmed on tekstifailis odavise.txt. """

def max_score(file_path):
    winner = ["", "", 0]
    try:
        with open(file_path) as fs:
            data = fs.readlines()
            for i in range(len(data)):
                data_split = data[i].split()
                if data_split[2] > data_split[3] and data_split[2] > data_split[4]:
                    max_points = data_split[2]
                    temp_winner = [data_split[0], data_split[1], max_points]
                elif data_split[3] > data_split[2] and data_split[3] > data_split[4]:
                    max_points = data_split[3]
                    temp_winner = [data_split[0], data_split[1], max_points]
                else:
                    max_points = data_split[4]
                    temp_winner = [data_split[0], data_split[1], max_points]

                if float(temp_winner[2]) > float(winner[2]):
                    winner = temp_winner
            print(f"Võitja on {winner[1].capitalize()} {winner[0].capitalize()}!\nPunktidega: {winner[2]}")
    except:
        print("error")
#max_score("schoolClass\\odavise.txt")

"""Ülesanne 3 Kassiklubi 
Kassiklubi Felix vajab abiprogrammi oma kiisukeste andmete töötlemiseks. Iga kassi kohta on andmefailis nimi, värvus ja saba pikkus. Viimane on eriti suure tähtsusega ;) 

Andmed on failis felix.txt 

Kirjuta programm, mis aitab klubi omanikul leida teda huvitavat värvi kasside keskmine sabapikkus. Programm peab laskma kasutajal värvi sisestada ja reageerima ka siis adekvaatselt, kui sellist värvi loomi polegi. """
def avg_cat_tail_length(color, file_path):
    summa = 0
    counter = 0
    with open(file_path) as fr:
        #fr.readlines()[0].split()[1]
        data = fr.readlines()
        for i in data:
            #print(i.split()[1])
            if i.split()[1] == color:
                counter += 1
                summa += int(i.split()[2])
        print(f"{color}, keskmine: {summa/counter}")

avg_cat_tail_length("valge", "schoolClass\\felix.txt")
