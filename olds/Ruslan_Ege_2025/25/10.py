def div(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if i != 7 and str(i)[-1] == '7':
                s.add(i)
            if str(n // i)[-1] == '7':
                s.add(n//i)
    if len(s) > 0:
        return min(s)
    else:
        return 0
for x in range(1125000, 1130000):
    d = div(x)
    if d != 0:
        print(x, d)