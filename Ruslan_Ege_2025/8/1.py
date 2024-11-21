import itertools
k = 0
for i in itertools.product('01234567', repeat = 5):
    s = ''.join(i)
    if s.count('3') <= 1 and s[0] != '0':
        can = True
        for x in range(len(s)-1):
            if int(s[x]) % 2 == 1 and int(s[x + 1]) % 2 == 1:
                can = False
        if can:
            k += 1

print(k)