import time
start = time.time()
for n in range(0,100):
    s = '>' + 17 * '0' + n * '3' + 17 * '2'
    while '>3' in s or '>2' in s or '>0' in s:
        if '>3' in s:
            s = s.replace('>3','22>',1)
        if '>2' in s:
            s = s.replace('>2','2>',1)
        if '>0' in s:
            s = s.replace('>0','3>',1)
    sum1 = sum(int(c) for c in s if c.isdigit())
    if sum1 ** 0.5 % 1 == 0:
        print(n)
finish = time.time()
print(finish - start)