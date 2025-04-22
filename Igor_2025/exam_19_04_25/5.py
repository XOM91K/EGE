def v3(n):
    r=''
    while n!=0:
        r+=str(n%3)
        n//=3
    return r[::-1]


res = []
for n in range(3, 100_000+1):
    r = v3(n)
    if n%3 == 0:
        r += r[-2:]
    else:
        r += v3(n%3 * 3)
    r = int(r, 3)
    if r<=150:
        res.append(n)

print(max(res))
