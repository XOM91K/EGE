l = [[int(d) for d in x.split()] for x in open("4.txt")]
ct = 0
for x in l:
  if x[0] != min(x) and x[0] != max(x) and x[-1] != min(x) and x[-1] != max(x):
      x.sort()
      if abs(x[0] - x[-1]) % abs(x[2] - x[3]) == 0:
          ct += 1
print(ct)