# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import os, random
os.system('cls' if os.name == 'nt' else 'clear')
while True:
      number = input('Введите число N : ')
      if number.isdigit() and int(number) > 0:
            number = int(number)
            grade = 0
            while  2 ** (grade) < number:
                  print(F" {2 ** (grade)} ", end='')
                  grade += 1
            print()
            print("Отрицательные степени двойки не включены в выборку")
            break
            

