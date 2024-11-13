import fnmatch
def dels(d):
  dls = []
  for x in range(1, int(d ** 0.5) + 1):
    if d % x == 0:
        dls.append(x)
        dls.append(d // x)
  dls = sorted(dls)
  if fnmatch.fnmatch(str(dls[-2]), "*6215"):
      return [True, dls[-2]]
  else:
      return [False, dls[-2]]

for x in range(23,10**6,23):
    g = dels(x)
    if x % 23 == 0:
        if g[0] == True:
          print(x, g[1])