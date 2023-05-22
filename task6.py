# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
#           где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
import os
os.system('cls' if os.name == 'nt' else 'clear')
def getSum(param):
      numberOf3digits = int(param)
      return int(numberOf3digits//100 + numberOf3digits%100//10 + numberOf3digits%10)
while True:
      number = input('Введите 6-ти значный номер билета : ')
      if number.isdigit() and len(number) == 6:
            number = int(number)
            if getSum(number//1000) == getSum(number%1000):
                  print("Билет счастливый! Поздравляем")
                  break
            else:
                  print("Биллет не счастливый.")
                  break
