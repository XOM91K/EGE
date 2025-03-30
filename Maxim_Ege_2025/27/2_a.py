l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], [], []]
for x in l:
    if -3 <= x[0] <= 0 and x[1] < 0.1:
        clusters[0].append(x)
    elif -1 <= x[0] <= 1.5 and 1.5 <= x[1] <= 6:
        clusters[1].append(x)
    elif 0.5 <= x[0] <= 3.1 and -5 <= x[1] <= 0:
        clusters[2].append(x)
corners = [[], [], []]
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
Px = int((corners[0][0] + corners[1][0] + corners[2][0]) / 3 * 10000)
Py = int((corners[0][1] + corners[1][1] + corners[2][1]) / 3 * 10000)
print(Px, Py)