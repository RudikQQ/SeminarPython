                                     #Task26
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

                                    #decision
# a = int(input("Введите число А: "))
# b = int(input("Введите число В: "))

# def func(a, b):
#     if b == 0:
#         return 1  


#     return a * func(a, b - 1)


# print(func(a, b))


                                   #Task28
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 
                                  #decision
# a = int(input("Введите число А: "))
# b = int(input("Введите число В: "))

# def recursive_sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return recursive_sum(a - 1, b + 1)


# print(recursive_sum(a, b))