while True:
        number = input('Введите целое положительное число: ')  # Ввод числа
        if number.isdigit() and len(number) == 3:
            number = int(number)
            print(F"Сумма цифр в числе составляет: {number//100 + number%100//10 + number%10}")
            break