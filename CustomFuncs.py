def LastFibo(n) :                         #Функция для  Числа Фибоначи 
    print(n)
    if n in [0, 1] :
        return n
    return LastFibo(n-1) + LastFibo(n-2)

def input_array(size):                    #Функция для создание списка
    array = []
    for i in range(size) :
        input_element1 = int(input(f'{i + 1} элемент массива: '))
        array.append(input_element1)
    return array

def pairs_count(array):                   #Функция для нахождения  пар в списке
    count = 0
    for n in set(array):
        count += array.count(n) // 2
    return count

def sum_of_dividers(num):                 #Функция для определения суммы делителей
    sum = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0 :
            sum += i
    return sum

def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])



def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])