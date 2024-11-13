import fnmatch
def is_prime(d):
    g = []
    for x in range(1, d + 1):
        if d % x == 0:
            g.append(x)
    return len(g)

for x in range(1,10**7,1):
  if fnmatch.fnmatch(str(x),"3?1111*"):
      if is_prime(x) == 2:
          print(x)