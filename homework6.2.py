str_1 = str(input("Введите первую строку:"))
str_2 = str(input("Введите вторую строку:"))

str_3 = str(input("Введите третью строку:"))
str_4 = str(input("Введите четвертую строку:"))

with open("second.py","w") as new_file:
    new_file.write(str_1 + "\n" + str_2 + "\n")
with open("second.py","a") as new_file:
    new_file.write(str_3 + "\n" + str_4 + "\n")