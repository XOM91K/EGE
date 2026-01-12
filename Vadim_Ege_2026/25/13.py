def f(x):
  s = []
  for d in range(2,int(x**0.5)+1):
    if x%d==0:
      s.append(d)
      s.append(x//d)
  return sum(set(s))
def isPrime(x):
  for d in range(2,int(x**0.5)+1):
    if x%d==0:
      return False
  return x>1
c = 0
for x in range(1_000_000,10_000_000):
  q = f(x)
  if isPrime(q):
    c+=1
    print(x,q)
  if c == 5:
    break

# 1000020	2201387
# 1000054	653641
# 1000056	1500143
# 1000066	532093
# 1000078	504289