import math
d = -1
sm = 0
while d != 0:
    d = int(input())
    if math.log2(d) % 1 == 0:
        print(sm)
        break
    if math.sqrt(d) % 1 == 0:
        continue
    if math.log2(d) % 1 == 0 and math.sqrt(d) % 1 == 0:
        print(sm)
        break
    sm += d
else:
    print(sm)
#print(2.5 % 1)