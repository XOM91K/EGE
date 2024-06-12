s = open(r'30.txt').readline().split('E')
dl_s = 10 ** 100
print(s)
for x in range(len(s) - 238):
    dl = 0
    for y in range(239):
        dl += len(s[x + y])
    dl_s = min(dl_s, dl + 240)
print(dl_s)