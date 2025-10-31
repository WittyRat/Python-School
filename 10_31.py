import random

number_list = [random.randint(0, 10) for _ in range(100)]
#number_list.sort()
#number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#number_list = [64, 34, 25, 12, 22, 99, 90]
print("Algne massiiv:", number_list)
print("===================================")


def bubble_sort():
    for i in range(len(number_list)):
        swapped = False
        for j in range(len(number_list)-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
                swapped = True
                #print(number_list, "\n=============")
                print(number_list)
                #time.sleep(0.5)
        if not swapped:
            print("Massiiv on sorteeritud")
            break

def is_it_sorted():
    for i in range(len(number_list)-1):
        if number_list[i] > number_list[i+1]:
            return False
    return True

#bubble_sort()
#is_it_sorted()
#print(is_it_sorted())
def sort_1():
    for i in range(len(number_list)-1):
        min_index = i
        for j in range(i+1, len(number_list)):
            if number_list[j] < number_list[min_index]:
                min_index = j
        number_list.insert(i, number_list.pop(min_index))
        print(number_list)
    print("Lõpp tulemus: ", number_list)

def sort_2():
    sorted_list = []
    for i in range(len(number_list)):
        min_value = min(number_list)
        number_list.pop(number_list.index(min_value))
        sorted_list.append(min_value)
        print(sorted_list)

#sort_1()
#print("=========")
#sort_2()

#print("Keskmine element on:", middle_index)
#print(number_list[middle_index])
def binary_search():
    found = False
    under_index = 0
    over_index = len(number_list) - 1
    find_number = int(input("Sisesta otsitav arv: "))
    while not found and under_index <= over_index:
        middle_index = (under_index+over_index) // 2
        if find_number > number_list[middle_index]:
            under_index = middle_index + 1
        elif find_number < number_list[middle_index]:
            over_index = middle_index - 1
        else:
            found = True

    if found:
        print("Leitud number", middle_index, "kohalt.")
    else:
        print("Ei leitud numbrit")
        print(number_list)
#binary_search()



#print(len(number_list))
counts = {}
for i in number_list:
    counts[i] = counts.get(i, 0) + 1

for number_list in sorted(counts):
    print("Arvu", number_list, "tuli", counts[number_list], "korda")


#print(counts[1])