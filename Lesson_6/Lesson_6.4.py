'''
Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ. Только теперь не нужно
создавать словарь с данными. Вместо этого нужно сохранить объединенные
данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО
'''

users_line_count = sum(1 for line in open('users.csv', 'r', encoding='utf-8'))
hobbies_line_count = sum(1 for string in open('hobby.csv', 'r', encoding='utf-8'))

if users_line_count < hobbies_line_count:
    exit(1)
else:
    with open('users_hobby.txt', 'a', encoding='utf-8') as users_hobby:
        users = (human for human in open('users.csv', 'r', encoding='utf-8'))
        hobbies = (activity for activity in open('hobby.csv', 'r', encoding='utf-8'))
        for iteration in range(users_line_count):
            try:
                name = next(users).strip()
                hobby = next(hobbies)
            except StopIteration:
                hobby = None
            users_hobby.write(f'{name}: {hobby}')
