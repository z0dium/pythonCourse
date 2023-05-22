# Задача 2: Найдите сумму цифр трехзначного числа.
import os
os.system('cls' if os.name == 'nt' else 'clear')
while True:
        number = input('Введите целое трехзначное положительное число: ')
        if number.isdigit() and len(number) == 3:
            number = int(number)
            print(F"Сумма цифр в числе составляет: {number//100 + number%100//10 + number%10}")
            break