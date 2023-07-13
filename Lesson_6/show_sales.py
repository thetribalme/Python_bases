import sys

if len(sys.argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as all_sales:
        print(all_sales.read())
else:
    with open('bakery.csv', 'r', encoding='utf-8') as slice_sales:
        if len(sys.argv) == 2:
            print(*slice_sales.read().split()[int(sys.argv[1]) - 1:], sep='\n')
        else:
            print(*slice_sales.read().split()[int(sys.argv[1]) - 1:int(sys.argv[2])], sep='\n')
