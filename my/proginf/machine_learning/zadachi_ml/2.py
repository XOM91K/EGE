dots = [[float(d.replace(',','.')) for d in x.split()] for x in open('2.txt')]
A, B = dots[0]
sm_rast = 0
for x, y in dots[1:]:
    sm_rast += ((A - x) ** 2 + (B - y) ** 2) ** 0.5
print(int(sm_rast))