import itertools
def v7(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]
def v5(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]
ct= 0
for i in range(1, 1_000_000):
    if len(v7(i)) <= 7 and hex(i)[2:][-1] == 'f':
        can = False
        for j in itertools.permutations(v5(i)):
            j = ''.join(j)
            if j == j[::-1]:
                can = True
                break
        if can:
            ct += 1
            print(v5(i))
            print(ct)
