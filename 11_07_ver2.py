#::-1
#casefold()
import string

#translation table
translation = str.maketrans('', '', '",.;:!?-')

fr = open("palindroom/paltest.05.sis", "r")
text = fr.readlines()

text_one = text[1].casefold().translate(translation).split()
text_two = text[1][::-1].casefold().translate(translation).split()
text_one_all = ""
text_two_all = ""
for i in range(len(text_one)):
    text_one_all += text_one[i]
    text_two_all += text_two[i]

print(text_one_all)
print(text_two_all)


if text[1].strip() == text[1][::-1].strip():
    print("tõene")
elif text[1].strip() != text[1][::-1].strip():
    print("väär")



fr.close()











print("")

fr = open("palindroom/paltest.01.sis", "r")

lines = fr.readlines()

fr.close()
fr = open("palindroom/paltest.01.val", "w")
for each in range(1, len(lines)):
    if lines[each].strip() == lines[each][::-1].strip():
        fr.write("TRUE\n")
        print("TÕENE")
    else:
        fr.write("FALSE\n")
        print("VÄÄR")
fr.close()
    






