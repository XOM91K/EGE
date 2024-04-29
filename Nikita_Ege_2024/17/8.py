l = [int(x) for x in open('8.txt')]
otv = 0
mx = 0
mx_pair = 0
for i in l:
    if len(str(abs(i))) == 2:
        mx = max(mx, i)
for i in range(len(l)-1):
    if (len(str(abs(l[i]))) == 2 or len(str(abs(l[i + 1]))) == 2) and (l[i] + l[i+1] <= mx):
        otv += 1
        mx_pair = max(mx_pair, l[i] + l[i + 1])
print(otv, mx_pair)