'''
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения —
данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ
'''
import json

names_and_hobbies = {}

with open('users.csv', 'r', encoding='utf-8') as users:
    names = users.read().splitlines()

with open('hobby.csv', 'r', encoding='utf-8') as activities:
    hobbies = activities.read().splitlines()

if len(names) < len(hobbies):
    exit(1)
else:
    for i in range(len(names)):
        try:
            names_and_hobbies[names[i]] = hobbies[i]
        except IndexError:
            names_and_hobbies[names[i]] = None

# writing file in .txt
with open('combined_file.txt', 'w', encoding='utf-8') as result_txt:
    result_txt.writelines(str(names_and_hobbies))

# writing file in .json
with open('combined_file.json', 'w', encoding='utf-8') as result_json:
    json.dump(names_and_hobbies, result_json)