'''
Задание 1. Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Задание 2. Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
'''
import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
file_extension = '.txt'
answer = requests.get(url)

primal_file_name = url.split('/')[-1]
if file_extension not in primal_file_name:
    filename = f'{primal_file_name}{file_extension}'
else:
    filename = primal_file_name

with open(filename, 'wb') as f:
    f.write(answer.content)

# task 1
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in file)
    for info in content:
        print(info)

# task 2
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    ip_list = [line.split()[0] for line in file]
    unique_ips = set(ip_list)
    max_count, spammer_ip = 0, 0
    for ip in unique_ips:
        ip_count = ip_list.count(ip)
        if ip_count > max_count:
            spammer_ip = ip
            max_count = ip_count
    print(f'Spammer IP: {spammer_ip}, number of requests: {max_count}')
