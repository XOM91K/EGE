s = open('2.txt').readline().replace('XYZ', '#')
k = 0
while k * '#' in s:
    k += 1
k -= 1
s = s.replace('#' * k, '%')
for x in range(len(s) - 2):
    if s[x] == '%':
        print(s[x], s[x + 1], s[x + 2], k * 3)