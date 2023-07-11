'''
Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных
файлов и имя выходного файла. Проверить работу скрипта
'''
import sys


def line_by_line_combining(first_input_file_name: str, second_input_file_name: str, output_file_name: str):
    users_line_count = sum(1 for _ in open(first_input_file_name, 'r', encoding='utf-8'))
    hobbies_line_count = sum(1 for _ in open(second_input_file_name, 'r', encoding='utf-8'))
    if users_line_count < hobbies_line_count:
        return 'Process finished with exit code 1'
    else:
        with open(output_file_name, 'a', encoding='utf-8') as users_hobby:
            users = (human for human in open(first_input_file_name, 'r', encoding='utf-8'))
            hobbies = (activity for activity in open(second_input_file_name, 'r', encoding='utf-8'))
            for iteration in range(users_line_count):
                try:
                    name = next(users).strip()
                    hobby = next(hobbies)
                except StopIteration:
                    hobby = None
                users_hobby.write(f'{name}: {hobby}')
        return f'{output_file_name} formed successfully'


print(line_by_line_combining(sys.argv[1], sys.argv[2], sys.argv[3]))
# I ran this module in PyCharm Terminal with
# >>> python Lesson_6.5.py users.csv hobby.csv users_hobby_adv.txt
