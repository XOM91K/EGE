mn = 10 ** 10
for n in range(11, 1000):
    trch = ''
    while n != 0:
        trch += str(n % 3)
        n //= 3
    trch = trch[::-1]
    if trch.count('0') + trch.count('2') > trch.count('1'):
        trch = '22' + trch
    else:
        trch = '11' + trch
    des = int(trch, 3)
    if des > 100:
        mn = min(des, mn)
print(mn)