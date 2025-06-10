

f = {}
for n in range(50_000+1):
    if n < 20:
        f[n] = n
    else:
        f[n] = (n-6) * f[n-7]


print((f[47_872] - 290 * f[47_865])/f[47_858])