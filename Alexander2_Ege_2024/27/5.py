l = [int(x) for x in open('5.txt')]
mn_sm = 10 ** 100
old_sm = 10 ** 100
for i in range(951_970, len(l)):
    sm = 0
    for j in range(len(l)):
        if abs(i - j) > len(l) / 2:
            sm += abs(len(l) - abs(i - j)) * l[j]
        else:
            sm += abs(i - j) * l[j]
    if old_sm < sm:
        print(sm, '+++++')
    else:
        print(sm, '-----')
    old_sm = sm
print(mn_sm)