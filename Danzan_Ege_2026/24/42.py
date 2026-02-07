s = open(r'C:\Users\Zarif\Downloads\1628_1 (2).txt').readlines()
rasts = []
for x in s:
    x = x.strip()
    if x.count('A') < 25:
        for y in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            rasts.append(x.rindex(y) - x.index(y))
print(max(rasts))