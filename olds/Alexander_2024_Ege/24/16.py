l = open("16.txt").readline().strip()
l = l.replace("4", "a")
l = l.replace("3", "e")
print(l)
s = "yandex"
c = 0
i = 0
mx = 0
for x in range(len(l)):
    if l[x] == s[c % 6]:
        c += 1
    else:
        mx = max(mx, c)
        c = 0
print(mx)
