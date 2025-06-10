a = 1
mx = -99999
mn = 99999
while a != 99999:
    a = float(input())
    if -10000 <= a <= 10000:
        mx = max(mx, a)
        mn = min(mn, a)
    else:
        print('Введите корректное число')
print(mx, mn)