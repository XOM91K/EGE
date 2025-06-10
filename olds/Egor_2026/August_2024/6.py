s = input() + '1'
l = []
ct = 0
for i in s:
    if i == '0':
        ct += 1
    elif i == '1':
        l.append(ct)
        ct = 0
print(l)