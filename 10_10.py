import time
import datetime
import calendar
#a) Sisestatakse tekstilõik ja otsitav sõna. Programm leiab, kas tekstilõigus on olemas otsitav sõna ja annab vastuseks, "Sõna ei leidnud" või "Sõna algas ... positsioonist". 

#b) Sisestatakse tekstilõik, otsitav sõna ja asendussõna. Programm uurib, kas otsitav sõna on olemas. Kui jah, siis asendab selle sõna asendussõnaga ja trükib teksti uuesti välja, vastasel juhul annab teate, et otsitavat sõna ei leitud ja asendamist ei toimu. 

#Abiks on meetodid str.find(), str.replace().

def ul_1():
    text = input("Sisesta tekstilõik: ")
    word = input("Sisesta otsitav sõna: ")

    #text.find(word)
    if text.find(word) == -1:
        print("Sõna ei leidnud")
    else:
        print("Sõna algas positsioonist", text.find(word))

def ul_1_1():
    text = input("Sisesta tekstilõik: ")
    word = input("Sisesta otsitav sõna: ")
    replace_word = input("Sisesta asendussõna: ")
    if text.find(word) == -1:
        print("Otsitavat sõna ei leitud, asendamist ei toimu.")
    else:
        new_text = text.replace(word, replace_word)
        print(new_text)


# Näiteks muutes sõna "kala" sammuga 4, saame "oepe". Kui samm läheb üle tähestiku lõpu, jätkatakse liikumist algusest. Teise kirjelduse (Wikipedia) järgi tehakse nihe vasakule - siis saaks sõnast "kala" "gwhw".

#Programm küsib sõna (või ka lause), nihke ehk sammu ja teisendab sõna antud sammuga. Peab ka jälgima, et kirjavahemärgid, tühikud jms paika jääksid.

#Pakun siinkohal välja kaks erinevat põhimõtet, kuidas šifreerimisele läheneda.

#1. Kirjuta programmi algusesse tähestik. Leia šifreeritava tähe indeks (str.find()), lisa samm uue tähe indeksi leidmiseks ja leia vaste tähestikust. Kui lähed uue tähe indeksiga tähestiku servast üle, on kasu jäägist (jääk, mis tekib uue tähe indeksi jagamisel tähestiku pikkusega).

def ul_2():
    #krüpteerib Caesar šifreeringu
    text = input("Sisesta tekst: ")
    step = int(input("Sisesta samm: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""

    for i in range(len(text)):

        new_index = (alphabet.index(text[i]) + step) % len(alphabet)

        new_letter = alphabet[new_index]
        # leiab uue tähe tähestikust
        new_text = new_text + new_letter

    print(new_text)

def ul_2_1():
    #dekrüpteerib Caesar šifreeringu
    text = input("Sisesta caesar šifreeringuga tekst: ")
    step = int(input("Sisesta samm, mida kasutati šifreerimisel: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""

    for i in range (len(text)):

        new_index = (alphabet.index(text[i]) - step) % len(alphabet)
        new_letter = alphabet[new_index]
        new_text = new_text + new_letter
    print(new_text)

#ul_2()
#time.sleep(1)
#ul_2_1()

#Programmile sisendiks on kasutaja nimi ja Eesti Vabariigi kodaniku isikukood. 

#Leia isikukoodist sugu, sünnipäev, vanus ja trüki nad võimalikult viisakalt ekraanile. 

#Leia isikukoodi kontrollnumber ja otsusta selle järgi, kas isikukood on korrektne.

#Vanuse arvutamiseks on vaja tänast kuupäeva. Seda saab küsida moodulis time oleva funktsiooniga localtime(), näiteks nii: aeg = time.localtime() Funktsioon localtime() tagastab objekti klassist struct_time, milles on järgmised atribuudid (http://docs.python.org/3/library/time.html): 

# =====================================================
# ORIGINAL CODE (COMMENTED OUT)
# =====================================================
# def ul_3():
#     nimi = "Tanel Metshein"
#     isikukood = str(50412080294)
#     kuud = ["", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
# 
#     sugu = isikukood[0]
#     if sugu == "1":
#         sugu = "mees"
#         aastaeg_esimene = "18"
#     elif sugu == "2":
#         sugu = "naine"
#         aastaeg_esimene = "18"
#     elif sugu == "3":
#         sugu = "mees"
#         aastaeg_esimene = "19"
#     elif sugu == "4":
#         sugu = "naine"
#         aastaeg_esimene = "19"
#     elif sugu == "5":
#         sugu = "mees"
#         aastaeg_esimene = "20"
#     elif sugu == "6":
#         sugu = "naine"
#         aastaeg_esimene = "20"
#     else:
#         print("Vale esimene number isikukoodis")
#     print("Isiku sugu on", sugu.upper())
#     
#     kuu_number = int(isikukood[3:5])
#     kuu_paev = isikukood[5:7]
#     print("Sünnipäev on " + kuu_paev + ". " + kuud[kuu_number])
# 
#     aastaaeg_teine = isikukood[1:3]
#     #print(isikukood[1:3])
#     aastaaeg = aastaeg_esimene + aastaaeg_teine
#     #print(aastaaeg)
#     aasta = time.localtime()
#     vanus = aasta[0] - int(aastaaeg)
#     #print(vanus)can 
#     if aasta[1] < kuu_number or (aasta[1] == kuu_number and aasta[2] < int(kuu_paev)):
#         vanus = vanus - 1
#         print("Isik on", vanus, "aastat vana.")
#     else:
#         print("Isik on", vanus, "aastat vana.")
# 
#     #isikukoodi kontroll
#     array = [int(char) for char in isikukood]
#     #print(array)
#     summa = 1*array[0] + 2*array[1] + 3*array[2] + 4*array[3] + 5*array[4] + 6*array[5] + 7*array[6] + 8*array[7] + 9*array[8] + 1*array[9]
#     #print(summa)
#     jaak = summa % 11
#     #print (jaak)
#     #print(isikukood[10])
#     if str(jaak) == str(isikukood[10]):
#         print("Isikukood on korrektne.")

# =====================================================
# BEAUTIFIED VERSION
# =====================================================
def analyze_isikukood():
    """
    Analüüsib Eesti isikukoodi ja leiab:
    - Sugu
    - Sünnipäeva
    - Vanuse
    - Kontrollib isikukoodi korrektsust
    """
    # Andmete sisestamine
    nimi = "Tanel Metshein"
    isikukood = "50412080294"  # Fixed: 5=male 2000s, 04=year(2004), 12=December, 08=8th day
    
    # Estonian month names
    kuud = ["", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", 
            "juuli", "august", "september", "oktoober", "november", "detsember"]
    
    print(f"=== {nimi} isikukoodi analüüs ===")
    print(f"Isikukood: {isikukood}")
    print()
    
    # 1. SUGU JA SAJANDI MÄÄRAMINE
    first_digit = isikukood[0]
    
    if first_digit in ["1", "3", "5"]:
        sugu = "mees"
    elif first_digit in ["2", "4", "6"]:
        sugu = "naine"
    else:
        print("❌ Vale esimene number isikukoodis!")
        return
    
    # Determine century
    if first_digit in ["1", "2"]:
        century = 1800
    elif first_digit in ["3", "4"]:
        century = 1900
    elif first_digit in ["5", "6"]:
        century = 2000
    
    print(f"👤 Sugu: {sugu.upper()}")
    
    # 2. SÜNNIPÄEVA LEIDMINE
    year_part = isikukood[1:3]    # Positions 1-2: year (04 = 2004)
    month_number = int(isikukood[3:5])  # Positions 3-4: month (12 = December)
    day = isikukood[5:7]          # Positions 5-6: day (08 = 8th)
    birth_year = century + int(year_part)
    
    print(f"🎂 Sünnipäev: {day}. {kuud[month_number]} {birth_year}")
    
    # 3. VANUSE ARVUTAMINE
    current_time = time.localtime()
    current_year = current_time[0]
    current_month = current_time[1]
    current_day = current_time[2]
    
    age = current_year - birth_year
    
    # Adjust age if birthday hasn't occurred this year
    if (current_month < month_number or 
        (current_month == month_number and current_day < int(day))):
        age -= 1
    
    print(f"📅 Vanus: {age} aastat")
    
    # 4. ISIKUKOODI KONTROLLNUMBRI KONTROLLIMINE
    digits = [int(char) for char in isikukood]
    
    # Calculate checksum using first 10 digits
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    checksum = sum(digit * weight for digit, weight in zip(digits[:10], weights))
    
    remainder = checksum % 11
    check_digit = int(isikukood[10])
    
    if remainder < 10:
        expected_check = remainder
    else:
        # If remainder is 10 or 11, use second algorithm
        weights2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        checksum2 = sum(digit * weight for digit, weight in zip(digits[:10], weights2))
        remainder2 = checksum2 % 11
        expected_check = 0 if remainder2 >= 10 else remainder2
    
    print()
    if check_digit == expected_check:
        print("✅ Isikukood on KORREKTNE!")
    else:
        print(f"❌ Isikukood on VIGANE! Oodatud kontrollnumber: {expected_check}, saadud: {check_digit}")


# Main function that calls the beautified version
def ul_3():
    """Legacy function name - calls the beautified version"""
    analyze_isikukood()


ul_3()