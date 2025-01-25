N = int(input())
ct = 0
for n in range(N):
    m = int(input())
    s = int(input())
    if m * 60 + s <= 18 * 60 + 30:
        ct += 1
print(ct)