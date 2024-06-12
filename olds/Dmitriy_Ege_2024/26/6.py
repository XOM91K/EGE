l = sorted([[int(d) for d in x.split()] for x in open('6.txt')])
time_opened = -1
time_waited = 0
ct = 0
for x in l:
    if x[0] - 1 > time_opened:
        time_waited += (x[0] - 1) - time_opened
        ct += 1
    time_opened = max(time_opened, x[1])
print(time_waited + (1439 - time_opened), ct + 1)