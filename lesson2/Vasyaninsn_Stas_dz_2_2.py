# Создаем переменную для списка:
one_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Добавляем кавычки до и кавычки после элемента списка являющимся числом:
a = 0
while a < len(one_list):
    if one_list[a].isdigit() or one_list[a].startswith('+'):
        one_list.insert(a, "\"")
        one_list.insert(a + 2, "\"")
        a += 1
    a += 1
# Дополняем нулём до двух целочисленных разрядов:
b = 0
while b < len(one_list):
    if one_list[b].isdigit():
        one_list[b] = one_list[b].zfill(2)
    elif one_list[b].startswith('+'):
        one_list[b] = one_list[b].zfill(3)
    b += 1
print(one_list)

print('-' * 100) # Разделяю блоки задания

# Сформировать из обработанного списка строку:
print(' '.join(one_list))


