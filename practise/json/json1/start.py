# рассмотрим формат передачи данных json
# в python json можно кодировать (сериализовать)
# или декодировать (десериализовать)
# команда dump(arg1, arg2) записывает в файл
# команда dumps(arg1) записывает в переменную


import json


data = {
    "name": "Kostan",
    "age": 32,
    "color": "red",
    "specification": [1, 2, 3]
}

data_clone = {
    "name": "Tolan",
    "age": 42,
    "color": "red",
    "specification": [7, 2, 3]
}

# первый способ записи в файл
with open("data.json", "w") as file:
    json.dump(data, file)

# второй способ записи в файл
temp_file = open("data.json", "w")
json.dump(data_clone, temp_file)




