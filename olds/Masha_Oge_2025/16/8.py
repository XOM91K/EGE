N = int(input())
final = 18 * 60 + 30
ct = 0
for x in range(N):
    m = int(input())
    s = int(input())
    if m * 60 + s <= final:
        ct += 1
print(ct)