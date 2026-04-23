a = int(input())
sm = 0
ct = 0
for x in range(a):
    n = int(input())
    if n > 0:
        sm += n
        ct += 1
print(sm / ct)
print(ct)