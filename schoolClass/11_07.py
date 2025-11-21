import os

input_path = "C:/Users/Tanel/Documents/Python School/keskmised_skoorid/input"
input_dir_list = os.listdir(input_path)
#print(input_dir_list[2])

output_path = "C:/Users/Tanel/Documents/Python School/keskmised_skoorid/output"
output_dir_list = os.listdir(output_path)
#print(output_dir_list[2])




for number in range(0, len(input_dir_list)):

    fr = open("keskmised_skoorid/input/"+str(input_dir_list[number]), "r")

    dict = {}
    i = 0
    for line in fr:
        list = line.strip().split()
        dict[i] = list
        i += 1

    rounds = dict[0]
    m_total = 0
    m_counter = 0
    j_total = 0
    j_counter = 0

    for j in range(1, len(dict)):
        if dict[j][0] == "M":
            m_total += int(dict[j][1])
            m_counter += 1
    #print(m_total)
    #print(m_counter)

    for j in range(1, len(dict)):
        if dict[j][0] == "J":
            j_total += int(dict[j][1])
            j_counter += 1
    #print(j_total)
    #print(j_counter)

    if m_counter == 0:
        m_avg = 0
    else:
        m_avg = m_total/m_counter
    if j_counter == 0:
        j_avg = 0
    else:
        j_avg = j_total/j_counter

    fr.close()
    fr = open("keskmised_skoorid/output/"+str(output_dir_list[number]), "w")
    #print("keskmised_skoorid/output/"+str(output_dir_list[0]))

    if m_avg == j_avg:
        print("keskmine skoor on mõlemal võrdne")
        fr.write("Vi")
    elif m_avg > j_avg:
        print("Mari keskmine skoor on suurem")
        fr.write("Ma")
    else:
        print("Jüril on keskmine skoor kõrgem")
        fr.write("Ju")
    fr.close()

print("") #pannes breakpoint siia, näitab muutujaid "variables" all

for each in range(0, len(output_dir_list)):
    print(output_dir_list[each])
    fr = open("keskmised_skoorid/output/"+str(output_dir_list[each]), "r")
    print(fr.read()+"\n")
    fr.close()


