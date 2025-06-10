l = [int(x) for x in open('8.txt')]
print(l)
mn17 = min([x for x in l if x % 17 == 0 and len(str(abs(x))) == 4])
print(mn17)
ct = 0
d = []
for x in range(len(l) - 2):
    dlina1 = len(str(abs((l[x]))))
    dlina2 = len(str(abs((l[x+1]))))
    dlina3 = len(str(abs((l[x+2]))))
    last1 = str(l[x])[-2:]
    last2 = str(l[x+1])[-2:]
    last3 = str(l[x+2])[-2:]
    if (dlina1 == 4 and last1 == "27") or (dlina2 == 4 and last2 == "27") or (dlina3 == 4 and last3 == "27"):
        KVtroyki = int(l[x])**2 + int(l[x+1])**2 + int(l[x+2])**2
        sum_troyki = abs(int(l[x])) + abs(int(l[x+1])) + abs(int(l[x+2]))
        if KVtroyki <= mn17 ** 2:
            ct += 1
            d.append(sum_troyki)
print(ct,min(d))