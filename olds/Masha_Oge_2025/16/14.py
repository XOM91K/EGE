a = int(input())
f = []
for x in range(a):
    b = int(input())
    if b % 5 == 0:
        f.append(b)
print(max(f))