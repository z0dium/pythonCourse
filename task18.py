# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input("Введите число N: "))
data = input(F"Введите {n} целых чисел (разделитель пробел): ").split()
x = int(input("Введите число X: "))
delta = abs(x-int(data[0]))
result = int(data[0])
for i in data:
    if abs(int(i) - x) < delta:
        delta = abs(int(i) -x)
        result = int(i)
print(result)