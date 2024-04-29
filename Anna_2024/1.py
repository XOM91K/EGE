n = int(input())
s = ''
for i in range(1, n + 1):
    if i % 2 != 0:
        s += str(i) + '-'
    else:
        s += str(i) + '+'
print(eval(s[:-1]))