import string
d = []
s = open('46.txt').readlines()
for x in s:
    x = x.strip()
    if x.count('A') < 25:
        for y in string.ascii_uppercase:
            d.append(x.rindex(y) - x.index(y))
print(max(d))