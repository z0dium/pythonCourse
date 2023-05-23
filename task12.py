# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#            a Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import os, random
os.system('cls' if os.name == 'nt' else 'clear')
while True:
      x, y = input('Введите через пробел 2 натуральных числа: сумму и произведение загаданных чисел : ').split()
      if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            discriminant = int(x*x - 4*y)
            number1 = 0
            number2 = 0
            if discriminant > 0:
                  number1 = ((x) + discriminant ** (0.5))/2
                  number2 = ((x) - discriminant ** (0.5))/2
                  if number2//1 == number2 and number1//1 == number1 and number1 > 0 and number2 > 0:
                        print(F"Петя задумал {int(number1)} и {int(number2)}")
                        break
            elif discriminant == 0:
                  number1 = number2 = int((x)/2)
                  if number2//1 == number2 and number1//1 == number1 and number1 > 0:
                        print(F"Петя задумал {int(number1)} и {int(number2)}")
                        break
            else:
                  print("Петя предложил плохие числа")
                  break


