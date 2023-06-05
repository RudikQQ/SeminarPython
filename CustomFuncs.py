def LastFibo(n) :                         #Функция для  Числа Фибоначи 
    print(n)
    if n in [0, 1] :
        return n
    return LastFibo(n-1) + LastFibo(n-2)

