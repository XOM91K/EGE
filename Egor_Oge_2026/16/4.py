# https://examinf.ru/tasks/980
n = int(input())
ct = 0
for i in range(n):
    m = int(input())
    s = int(input())
    if m * 60 + s <= 18 * 60 + 30:
        ct += 1
print(ct)