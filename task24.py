# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

gryadka = open("task24_input_file.txt","r").read()
print (F"Грядка (с количеством ягод на каждом кусте): ", gryadka)
gryadka = gryadka.split()
qty = len(gryadka)
for i in range(0,qty):
    gryadka[i] = int(gryadka[i])
berriesFrom3bushes = []
for i in range(0,qty):
    berriesFrom3bushes.append(gryadka[(qty-1 + i)%qty] + gryadka[i] + gryadka[(qty + 1 + i)%qty])
print("Максимальное число ягод, которое можно собрать за 1 заход: ", sorted(berriesFrom3bushes).pop())
