l = [int(x) for x in open('20.txt')]
ans = 0
a = 0
d = max([x for x in l if x % 100 == 37])
print(d)
for x in range(len(l) - 3):
    n1 = l[x]
    n2 = l[x + 1]
    n3 = l[x + 2]
    n4 = l[x + 3]
    if (n1 > d) + (n2 > d) + (n3 > d) + (n4 > d) == 2:
        if ((n1 % 100) % 11 == 0) + ((n2 % 100) % 11 == 0) + ((n3 % 100) % 11 == 0) + ((n4 % 100) % 11 == 0) == 1:
            ans += 1
            for n in (n1, n2, n3, n4):
                if (n % 100) % 11 == 0:
                    a += n
print(ans, a)
