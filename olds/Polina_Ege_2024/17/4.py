l = [int(x) for x in open('17_3.txt')]
ct = 0
mn = 10**10
for x in range(len(l) - 2):
    if sum([int(x) for x in str(l[x])[-1::-2]]) == 0:
        ch1 = False
    else:
        ch1 = sum([int(x) for x in str(l[x])[-2::-2]]) % sum([int(x) for x in str(l[x])[-1::-2]]) == 0
    if sum([int(x) for x in str(l[x + 1])[-1::-2]]) == 0:
        ch2 = False
    else:
        ch2 = sum([int(x) for x in str(l[x + 1])[-2::-2]]) % sum([int(x) for x in str(l[x + 1])[-1::-2]]) == 0
    if sum([int(x) for x in str(l[x + 2])[-1::-2]]) == 0:
        ch3 = False
    else:
        ch3 = sum([int(x) for x in str(l[x + 2])[-2::-2]]) % sum([int(x) for x in str(l[x + 2])[-1::-2]]) == 0
    if ch1 and ch2 and ch3:
        mn = min(mn, l[x] + l[x + 1] + l[x + 2])
        ct += 1

print(ct, mn)