N = 0
sm = 0
ct = 0
while abs(N) % 10 != 1 and abs(N) % 10 != 5:
    N = int(input())
    if abs(N) % 10 == 1 or abs(N) % 10 == 5:
        break
    sm += N
    ct += 1
print(sm / ct)