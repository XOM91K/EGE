l = sorted([[int(d) for d in x.split()] for x in open('5.txt')])
print(l)
last_client = 0
sm = 0
ct = 1
for x in l:
    if x[0] - last_client > 1:
        ct += 1
        sm += x[0] - last_client - 1
    last_client = max(last_client, x[1])
print(ct, sm + (1440 - last_client))
