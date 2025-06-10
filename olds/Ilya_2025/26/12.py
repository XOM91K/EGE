l = [[int(d) for d in x.split()] for x in open('12.txt')]
l = sorted(l, key=lambda d: d[1])
aud_time = 0
ct_l = []

for x in l:
    if x[0] >= aud_time:
        aud_time = x[1]
        ct_l.append(x)
        if len(ct_l) % 3 == 0:
            aud_time += 10
for x in ct_l:
    print(x)
#26

#[1199, 1221]
#[1246, 1259] #[1257, 1262]
#[1264, 1273] #[1272, 1298]

#
print(57 - 21)
print(sorted(l))