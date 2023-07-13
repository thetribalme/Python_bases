from decimal import Decimal as Dec
import sys

with open('bakery.csv', 'a', encoding='utf-8') as bakery_sales:
    desired_amount = Dec(sys.argv[1]).quantize(Dec('1.00'))
    bakery_sales.write(f'{desired_amount}\n')
print(sum(Dec(line.strip()) for line in open('bakery.csv', 'r', encoding='utf-8')))

# I ran this module in PyCharm Terminal with
# >>> python add_sales.py 44444.33
