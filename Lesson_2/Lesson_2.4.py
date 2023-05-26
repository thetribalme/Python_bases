'''
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на
экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов
списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
'''
job_name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                 'директор аэлита']

# forming a new list
name_list = []

for i, v in enumerate(job_name_list):
    internal_list = v.split(' ')
    name_list.append(internal_list.pop())
    print(f'Привет, {name_list[i].capitalize()}!')

# without forming a new list
for i, v in enumerate(job_name_list):
    internal_list = v.split(' ')
    job_name_list[i] = internal_list.pop()
    print(f'Привет, {job_name_list[i].capitalize()}!')
