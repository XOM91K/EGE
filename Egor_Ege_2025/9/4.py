l = [sorted([int(d) for d in x.split()]) for x in open("4.txt")]
cnt = 0
for x in l:
    if len(set(x)) == 6:
      if (x[0] + x[-1]) / 2 < (x[1]+x[2]+x[3]+x[4]) / 4:
          cnt += 1
print(cnt)