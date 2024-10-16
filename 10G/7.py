n = int(input('Введите число: '))
dels = []
for x in range(1, n + 1):
    if n % x == 0:
        dels.append(x)
print(f'Количество делителей числа {n}: {len(dels)} {dels}')