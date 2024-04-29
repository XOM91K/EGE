l = [sorted([int(d) for d in x.split()]) for x in open('11.txt')]
ct = 0
for x in l:
    ct += 1
    if len(set(x)) == 5:
        print(x)
        povt = sum(x) - sum(set(x))
        if (sum(x) - povt * 2) / 4 <= povt * 2:
            print(ct, sum(x))
            break