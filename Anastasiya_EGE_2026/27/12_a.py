import math
l = [[float(d) for d in x.split()] for x in open('12_a.txt')]
clusters = [[], []]
for p in l:
    if p[1] > 0:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
mx_sm_rast = 0
dve_tochki = []
for p1 in clusters[0]:
    for p2 in clusters[1]:
        if math.dist(p1, p2) > mx_sm_rast:
            mx_sm_rast = math.dist(p1, p2)
            dve_tochki = [p1, p2]
print(abs(int((dve_tochki[0][0] + dve_tochki[1][0]) * 1000)))
print(int(abs((dve_tochki[0][1] - dve_tochki[1][1])) * 1000))