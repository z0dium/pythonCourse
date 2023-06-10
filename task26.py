# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = int(input())
B = int(input())

def power(n,m):
    if m == 0:
        return 1
    return n*power(n,m-1)

print(power(A,B))
