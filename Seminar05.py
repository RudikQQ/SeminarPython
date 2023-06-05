                      #Task 31
# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

                      #decision

# import CustomFuncs
# print(CustomFuncs.LastFibo(7))

# from CustomFuncs import *
# print(LastFibo(7))

                     #task33
# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
                     #decision
# a = [1, 3, 4, 5, 3, 2, 1, 3, 4]
# print(a)
# print(max(a))
# print(min(a))
# for i in range(len(a)):
#     if a[i] == max(a):
#         a[i] = min(a)
# print(a)        
                     #Task35
# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 
                     #decision
# numbers = int(input("Введите число"))
# def is_simple(numbers):
#     if numbers > 2 and numbers % 2 != 0 :
#         for i in range ( 3, numbers // 2 ):
#             if numbers % i == 0:
#                 return False 
#         return True    
#     else:
#         return False
    



#     11:30

