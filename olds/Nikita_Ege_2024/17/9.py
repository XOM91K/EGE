l = [int(x) for x in open('9.txt')]
otv = 0
sm = 0
mx = 0
sm = sum(l) / len(l)
for i in range(1, len(l)-2):
    if l[i]*l[i+1] > l[i-1]*l[i+2]:
        mx = max(mx, l[i]+l[i+1])
        if l[i] > sm or l[i+1] > sm:
            otv+= 1
print(mx)
print(otv)