n = int(input())
if 10 <= n <= 999:
    d = n
    last_digit = str(n)[0]
    d = int(str(n)[1:])
    d *= 10
    d += int(str(n)[0])
    print(d)