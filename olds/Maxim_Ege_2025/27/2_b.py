l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_b.txt')]
clusters = [[], [], [], [], []]
for x in l:
    if -60 <= x[0] <= -35 and x[1] < 40:
        clusters[0].append(x)
    elif -30 <= x[0] <= -7 and x[1] < 40:
        clusters[1].append(x)
    elif 0 <= x[0] <= 20 and x[1] < 40:
        clusters[2].append(x)
    elif -39 <= x[0] <= -22 and x[1] > 40:
        clusters[3].append(x)
    elif -12 <= x[0] <= 4 and x[1] > 40:
        clusters[4].append(x)
corners = [[], [], [], [], []]
ind = 0
for x in clusters:
    mx_sm_rast = 0
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += ((y[0] - z[0]) ** 2 + (z[1] - y[1]) ** 2) ** 0.5
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            corners[ind] = y
    ind += 1
print(corners)
Px = int((corners[0][0] + corners[1][0] + corners[2][0] + corners[3][0] + corners[4][0]) / 5 * 10000)
Py = int((corners[0][1] + corners[1][1] + corners[2][1] + corners[3][1] + corners[4][1]) / 5 * 10000)
print(Px, Py)