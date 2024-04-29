N = int(input())
ct = 0
for x in range(N + 1):
    if (x > 100 and x % 3 == 0) or (x % 5 == 0 and x < 100):
        ct += 1
print(ct)