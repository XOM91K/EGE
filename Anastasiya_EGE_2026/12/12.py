import time
start = time.time()
for x in range(1000): # перебираем x и y
    for y in range(1000):
        str1 = '0'*x + '1'*2*y + '2'*y # формируем нашу строку
        if len(str1) == 1000: # проверяем, что строка имеет именно 1000 символов
            sum1 = str1.count('1') + str1.count('2')*2 # считаем сумму исходной строки
            str2 = str1.replace('0','*').replace('1','+') # защита от наложения замен друг на друга
            str2 = str2.replace('2','1').replace('*','2').replace('+', '0')
            sum2 = str2.count('1') + str2.count('2')*2 # считаем сумму конечной строки
            if sum1+1640 == sum2:
                print(str1.count('0'), sum1, sum2)

finish = time.time()
print(finish - start)

