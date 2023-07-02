'''
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с
сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
'''
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [element for element in src if src.count(element) == 1]
print(result)
