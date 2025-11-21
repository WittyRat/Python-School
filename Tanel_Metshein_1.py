#Tanel Metshein
#print((241220 % 6)+1) = 3

"""Tekstifailis kt_2.txt on temperatuurid ja kuupäevad, millal selline temperatuur esines. Täpsemalt on tekstifaili esimesel real päevade arv ning igal järgneval real on kaks tühikuga eraldatud täisarvu: kuupäev ja temperatuur. Andmefail võib erineda näitest (nt sisaldada vähem ridu, esimene kirje ei pruugi olla kuupäeva 1 kohta jms).
Kirjutada programm nende päevade keskmise temperatuuri leidmiseks, kus kraadiklaas näitas külmakraade. Külmakraadide puudumisel väljastada sobiv teade."""

with open("kt_2.txt", "r") as f:
    counter = 0
    total_temp = 0
    data = f.readlines()
    for i in range(1, len(data)):
        if int(data[i].split()[1]) < 0:
            counter += 1
            total_temp += int(data[i].split()[1])
#print(counter)
#print(total_temp)
if counter == 0:
    print("Ei olnud ühtegi külmakraadidega päeva kuu jooksul")
else:
    avg_cold_temp = total_temp/counter
    print(f"Külmapäevade keskmine temperatuur oli {round(avg_cold_temp)} C")





