a = int(input())
b = int(input())
ct = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        ct += 1
print(ct)