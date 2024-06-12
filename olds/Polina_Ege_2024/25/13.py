def prime(n):
    for x in range(2, int(n ** 0.5 ) + 1):
        if n % x == 0:
            return False
    return True
for x in range(9998, 10 ** 7 + 1, 9998):
    if str(x)[0] == '9':
        if prime(int(str(x)[1:-1])) and str(x)[-1] != '':
            print(x, x // 9998)
