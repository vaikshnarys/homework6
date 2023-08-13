import json
dictionary = {
    111111 : ("Adam",32),
    222222 : ("Dima",20),
    333333 : ("Maksim",44),
    444444 : ("Olga",77),
    555555 : ("Yana",18),
    666666 : ("Kasia",13)
}

with open("first.json","w") as new_file:
    json.dump(dictionary,new_file,indent= 4)