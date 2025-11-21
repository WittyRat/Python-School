import time

student_list = [
    ("Charlie", 160),
    ("Heidi", 168),
    ("Bob", 175),
    ("Eve", 170),
    ("Grace", 185),
    ("Judy", 158),
    ("Frank", 155),
    ("David", 180),
    ("Ivan", 172),
    ("Alice", 165),
]

def lines():
    print("============================")

def ul_2():
    
    sum_height = 0

    #print(len(students))
    #print(students[0][1])

    for i in range(len(student_list)):
        sum_height = sum_height + int(student_list[i][1])
        print(sum_height)

    lines()

    middle_height = sum_height / len(student_list)
    print(middle_height, "on keskmine pikkus")

    lines()

    for i in range(len(student_list)):
        if int(student_list[i][1] < middle_height):
            print(student_list[i][0], "on keskmisest lühem")

    lines()

    max_height = max(student[1] for student in student_list)

    for i in range(len(student_list)):
        if int(student_list[i][1] == max_height):
            print(student_list[i][0], "on kõige pikem")

    lines()

    min_height = min(student[1] for student in student_list)

    for i in range(len(student_list)):
        if int(student_list[i][1] == min_height):
            print(student_list[i][0], "on kõige lühem")

    lines()

    name_find = input("Sisesta üliõpilase eesnimi, keda otsid: ")
    name_find = name_find.capitalize()
    #print(name_find)
    for i in range(len(student_list)):
        if student_list[i][0] == name_find:
            print(student_list[i][0], "on pikkusega", student_list[i][1], "cm")
            break
    else:
        print("Sellist üliõpilast andmebaasis ei ole")

#ul_2()

def ul_3():
    number_list = [5, 12, 7, 3, 9, 15, 21, 8, 4, 11]
    #print(n)
    for i in range(len(number_list)):
        swapped = False
        for j in range(len(number_list)-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
                swapped = True
                print(number_list, "\n=============")
                time.sleep(0.5)
        if not swapped:
            print("Massiiv on sorteeritud")
            break
#ul_3()


def ul_4():
    student_list.sort(reverse=True, key=lambda student: student[1])
    for i in range(len(student_list)):
        print(student_list[i])
    #print(student_list[1][1])
#ul_4()