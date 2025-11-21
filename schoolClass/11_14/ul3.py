
def value_counts(file_name):
    fr = open(file_name, "r", encoding="UTF-8")
    string = fr.read().lower()
    
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter
    fr.close()

def letters_percent(counting):
    keys = list(counting.keys())
    values = list(counting.values())
    letters_amount = 0
    for i in range(len(keys)):
        if keys[i].isalpha():
            letters_amount = letters_amount + values[i]

    percents = []
    for j in range(len(keys)):
        if keys[j].isalpha():
            percents += (values[j]/letters_amount)*100 #lisada uus kirje listi
            print(f"{keys[j]} on {round(((values[j]/letters_amount)*100), 3)}%")
            return percents


        
count = value_counts("11_14/inglise1.txt")
count1 = value_counts("11_14/eesti1.txt")
count2 = value_counts("11_14/saksa1.txt")
letters_percent(count)

        





