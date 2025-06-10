l = [int(x) for x in open('12.txt')]
su = []
d = []
k = 0
dvuz = []
quad = []
for x in l:
    if len(str(abs(x))) == 2:
        dvuz.append(x)
y = max(dvuz)
for x in range(len(l)-3):
    if str(l[x])[-1] == str(l[x+1])[-1] == str(l[x+2])[-1] == str(l[x+3])[-1]:
        quad.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
A = max(quad)
for x in range(len(l)-4):
    b = 0
    if l[x] < A:
        b += 1
    if l[x+1] < A:
        b += 1
    if l[x+2] < A:
        b += 1
    if l[x+3] < A:
        b += 1
    if l[x+4] < A:
        b += 1
    if b == 1:
      if (l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x+4]) % y == 0:
            k += 1
            su.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3]+l[x+4])
print(k,min(su))
