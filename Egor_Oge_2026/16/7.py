a = int(input())
ct = 0
for i in range(a):
    mins = int(input())
    seconds = int(input())
    if mins * 60 + seconds <= 18 * 60 + 30:
        ct += 1
print(ct)