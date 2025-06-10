d = int(input())
s = ''
alf = '0123456789abcdef'
while d > 0:
    s += alf[d % 16]
    d //= 16
print(s[::-1])