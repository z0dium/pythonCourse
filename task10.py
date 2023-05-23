# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
#            чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import os, random
os.system('cls' if os.name == 'nt' else 'clear')
while True:
      count = input('Введите число монеток: ')
      if count.isdigit() :
            count = int (count)
            orelCounter = 0
            reshkaCounter = 0
            for i in range(count):
                  drop = random.randrange(2)
                  if drop == 0:
                        reshkaCounter += 1
                  else:
                        orelCounter += 1
                  print(F"{drop} ", end='')
            print()      
            if orelCounter < reshkaCounter:
                  print(F"Количество монет для переворачивания: {orelCounter}.")
            else:
                  print(F"Количество монет для переворачивания: {reshkaCounter}.")
            break