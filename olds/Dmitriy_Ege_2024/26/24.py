#Задание 26 (№12495).(Л. Шастин)
l = sorted([int(x) for x in open('24.txt')])
l.insert(0, 0)
S = 1021000
b = 11111
zpk = []
for x in range(len(l) - 1):
    if b - (l[x + 1] - l[x]) < 0:
        zpk.append(l[x])
        b = 11111
    b -= (l[x + 1] - l[x])
mn = 10 ** 10
for x in range(len(l) - 1, -1, -1):
    if zpk[-2] < l[x] <= zpk[-1]:
        mn = min(mn, l[x])
print(len(zpk), mn)