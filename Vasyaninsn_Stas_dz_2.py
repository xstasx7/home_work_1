# Создаем список, состоящий из кубов нечётных чисел от 1 до 1000:
cube = []
for i in range(1, 1000, 2):
    cube.append(i**3)
print(cube)

print("-"*100) # Разделяю блоки задания
# Вычисляем сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7:
for i in cube:
    int_cube = sum(map(int,str(i)))
    if int_cube % 7 == 0:
        print(int_cube)

print("-"*100) # Разделяю блоки задания
# К каждому элементу списка добавляем 17:
sum_cube = []
for i in cube:
    sum_cube.append(i+17)
print(sum_cube)

print("-"*100) # Разделяю блоки задания
# Вычисляем сумму тех чисел из этого списка,сумма цифр которых делится нацело на 7:
for i in sum_cube:
    int2_cube = sum(map(int,str(i)))
    if int2_cube % 7 == 0:
        print(int2_cube)
