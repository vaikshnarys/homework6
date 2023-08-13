import json
import csv

numbers = {
    "Adam" : 48730046149,
    "Dima" : 4852066101,
    "Maksim" : 4866778902,
    "Olga" : 487939099,
    "Yana": 489039908,
    "Kasia": 4823040332
}
with open("first.json","r") as file:
    read_data = json.load(file)

with open("first.csv", "w", newline="") as new_file:
        main_names = ["id", "name", "age", "phone"]
        writer = csv.DictWriter(new_file, fieldnames = main_names)
        writer.writeheader()
        for id, (name, age) in read_data.items():
            phone = numbers.get(name, "")
            writer.writerow({'id': id, 'name': name, 'age': age, 'phone': phone})