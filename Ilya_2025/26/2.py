l = sorted([int(x) for x in open('2.txt')], reverse=True)
ct = 1
last_box = l[0]
for x in l:
    if abs(x - last_box) >= 3:
        last_box = x
        ct += 1
        print(x)
print(ct)