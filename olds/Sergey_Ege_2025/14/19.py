max8 = 0

for x in range(9,1000):
  l = []
  b = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
  while b > 0:
    l.append(b % x)
    b //= x
  l = l[::-1]
  if l.count(8) >= max8:
      max8 = l.count(8)
      print(x)