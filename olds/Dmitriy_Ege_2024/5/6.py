'''
Алгоритм получает на вход натуральное число N и строит по нему новое число R следующим образом:
1. Строится троичная запись числа N.
2. К этой записи дописываются разряды по следующему правилу. Если сумма троичных разрядов кратна 3, слева дописывается 20, иначе слева дописывается 10.
3. Полученная таким образом запись является троичной записью искомого числа R.
Например, для числа 10 троичная запись 1013 преобразуется в запись 101013 = 91, для числа 11 троичная запись 1023 преобразуется в 201023 = 173.
Укажите максимальное значение N, после обработки которого с помощью этого алгоритма получается число R, меньшее чем 100.
'''
def tr(n):
    s = ''
    while n > 0:
        s += str((n % 3))
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = tr(N) #1020102102020
    if sum(map(int, R)) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    if int(R, 3) < 100:
        print(N)