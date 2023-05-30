                        #task25

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
                         #decision
# text = input('Введите строку символов: ')
# my_list = text.split()
# dictonary = {}
# for i in my_list:
#     if i in dictonary.keys():
#       dictonary[i] += 1
#       print(f'{i}_{dictonary[i]}', end=' ')
#     else:
#       dictonary[i] = 0
#       print(i, end=' ')
        
                        #Task27
# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
                             #decision
# text = input('Введите предложение: ')
# my_list = set(text.split())
# print(len(my_list))
