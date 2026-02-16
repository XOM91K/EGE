l = [int(x) for x in open('5.txt')]
k = 820
l = sorted(l, key=lambda d: -d)
zach = l[:k + 1]
print(zach)
ind = 0
if zach[-1] == zach[-2]:
    ball = zach[-3]
else:
    ball = zach[-2]

last_student = zach[-2]
sm = 0
ct = 0
for x in l:
    if x < last_student:
        sm += x
        ct += 1
print(ball, sm // ct)