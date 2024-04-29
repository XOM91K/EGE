for x in range(3, 10001):
    n = '5' + x * '2'
    nn = 0
    while '52' in n or '2222' in n or '1112' in n:
        if '52' in n:
            n = n.replace('52', '11', 1)
            n = n.replace('2222', '5', 1)
        else:
            n = n.replace('1112', '2', 1)
    for i in range(len(str(n))):
        nn += int(n[i])
    if nn == 1685:
        print(x)