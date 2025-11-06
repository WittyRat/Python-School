import os

input_path = "C://Users//Tanel//Documents//Python School//keskmised_skoorid//input"
input_dir_list = os.listdir(input_path)
#print(input_dir_list[0])

output_path = "C://Users//Tanel//Documents//Python School//keskmised_skoorid//output"
output_dir_list = os.listdir(output_path)
#print(output_dir_list[0])

fr = open("keskmised_skoorid/input/"+str(input_dir_list[0]), "r")

dict = {}
i = 0
for line in fr:
    list = line.strip().split()
    dict[i] = list
    i += 1
fr.close()

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

m_avg = m_total/m_counter
j_avg = j_total/j_counter

fr = open("keskmised_skoorid/output/"+str(output_dir_list[0]), "w")
#print("keskmised_skoorid/output/"+str(output_dir_list[0]))

if m_avg == j_avg:
    print("keskmine skoor on mõlemal võrdne")
    fr.write("Va")
elif m_avg > j_avg:
    print("Mari keskmine skoor on suurem")
    fr.write("Ma")
else:
    print("Jüril on keskmine skoor kõrgem")
    fr.write("Ja")

fr.close()