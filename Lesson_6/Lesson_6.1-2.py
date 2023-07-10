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
# task 1
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    logs_list = []
    for line in file:
        listed_line_content = file.readline().split(' ')
        remote_addr = listed_line_content[0]
        request_type = listed_line_content[5].strip('"')
        requested_resource = listed_line_content[6]
        logs_list.append((remote_addr, request_type, requested_resource))

# task 2
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    ip_list = []
    for line in file:
        listed_line_content = file.readline().split(' -')
        ip_list.append(listed_line_content[0])
    unique_ips = set(ip_list)
    max_count, spammer_ip = 0, 0
    for ip in unique_ips:
        ip_count = ip_list.count(ip)
        if ip_count > max_count:
            spammer_ip = ip
            max_count = ip_count
    print(f'Spammer IP: {spammer_ip}, number of requests: {max_count}')
