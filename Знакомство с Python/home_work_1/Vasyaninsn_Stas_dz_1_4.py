# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


quarter_num = int(input("Введите номер четверти: "))
if quarter_num == 1:
    print("x > 0 and y > 0")
elif quarter_num == 2:
    print("x < 0 and y > 0")
elif quarter_num == 3:
    print("x < 0 and y < 0")
elif quarter_num == 4:
    print("x > 0 and y < 0")
else:
    print("Есть только 4 номера плоскости")
