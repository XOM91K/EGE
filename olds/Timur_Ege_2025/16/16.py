import functools
@functools.lru_cache(None)
def F(n):
  if n < 6:
      return n
  if n >= 6:
      return (3 * n - 2) * F(n - 5)
for x in range(1,60000):
        F(x)
print((F(20568) - 51702 * F(20563)) // F(20553))